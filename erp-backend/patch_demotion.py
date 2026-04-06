"""
Patch script: replaces _purge_student_year_data (deletes financial data - DANGEROUS)
with _deactivate_student_year_data (state transitions - ERP-safe), and adds the
/api/students/demote-bulk endpoint.
"""
import re

ROUTES_FILE = r"d:\E drive\Development\Projects\HIFZ ERP\MS Hifz Scientifc study Programm\HifzErpSoftwareApplication\erp-backend\routes\student_routes.py"

with open(ROUTES_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# ── 1. Replace _purge_student_year_data ──────────────────────────────────────
OLD_PURGE = (
    "def _purge_student_year_data(student_id, academic_year):\n"
    '    """\n'
    "    Remove data created in an accidentally promoted year so the student can be\n"
    "    restored to the previous academic year cleanly.\n"
    '    """\n'
    "    Attendance.query.filter_by(student_id=student_id, academic_year=academic_year).delete(\n"
    "        synchronize_session=False\n"
    "    )\n"
    "    StudentSubjectAssignment.query.filter_by(\n"
    "        student_id=student_id, academic_year=academic_year\n"
    "    ).delete(synchronize_session=False)\n"
    "    StudentTestAssignment.query.filter_by(\n"
    "        student_id=student_id, academic_year=academic_year\n"
    "    ).delete(synchronize_session=False)\n"
    "    StudentMarks.query.filter_by(student_id=student_id, academic_year=academic_year).delete(\n"
    "        synchronize_session=False\n"
    "    )\n"
    "    FeePayment.query.filter_by(student_id=student_id, academic_year=academic_year).delete(\n"
    "        synchronize_session=False\n"
    "    )\n"
    "    StudentFee.query.filter_by(student_id=student_id, academic_year=academic_year).delete(\n"
    "        synchronize_session=False\n"
    "    )\n"
)

NEW_DEACTIVATE = (
    "def _deactivate_student_year_data(student_id, academic_year, demoted_by_user_id=None):\n"
    '    """\n'
    "    ERP-safe demotion helper - uses state transitions, NEVER deletes financial data.\n"
    "\n"
    "    ERP Rule: Financial records must NEVER be deleted, even for corrections.\n"
    "    - StudentFee structures: deactivated (is_active=False, deleted_at set).\n"
    "    - FeePayment rows: UNTOUCHED - real collected money, permanent audit trail.\n"
    "    - Attendance rows: UNTOUCHED - historical calendar records.\n"
    "    - StudentMarks rows: UNTOUCHED - historical academic records.\n"
    "    - Subject/test assignments: deactivated (status=False).\n"
    '    """\n'
    "    now = datetime.now()\n"
    "    for fee in StudentFee.query.filter_by(student_id=student_id, academic_year=academic_year).all():\n"
    "        fee.is_active = False\n"
    "        fee.deleted_at = now\n"
    "        if demoted_by_user_id:\n"
    "            fee.deleted_by = demoted_by_user_id\n"
    "    for sa in StudentSubjectAssignment.query.filter_by(student_id=student_id, academic_year=academic_year).all():\n"
    "        sa.status = False\n"
    "    for ta in StudentTestAssignment.query.filter_by(student_id=student_id, academic_year=academic_year).all():\n"
    "        ta.status = False\n"
)

# Normalize CRLF
content_lf = content.replace("\r\n", "\n")
old_lf = OLD_PURGE.replace("\r\n", "\n")

if old_lf not in content_lf:
    # Try to find the function using regex as fallback
    print("Exact match not found - trying regex replacement...")
    pattern = r"def _purge_student_year_data\(student_id, academic_year\):.*?(?=\n\n\n|\ndef |\n@bp)"
    match = re.search(pattern, content_lf, re.DOTALL)
    if match:
        content_lf = content_lf[:match.start()] + NEW_DEACTIVATE.rstrip("\n") + content_lf[match.end():]
        print("Regex replacement succeeded")
    else:
        print("FAILED: Could not find _purge_student_year_data to replace")
        exit(1)
else:
    content_lf = content_lf.replace(old_lf, NEW_DEACTIVATE, 1)
    print("Exact replacement succeeded")

# ── 2. Fix references to _purge_student_year_data inside promote-bulk ────────
content_lf = content_lf.replace(
    "_purge_student_year_data(student_id, mistaken_year)",
    "_deactivate_student_year_data(student_id, mistaken_year, demoted_by_user_id=current_user.user_id)"
)
print("Updated reference in promote-bulk")

# ── 3. Inject demote-bulk endpoint before /api/students/summary ──────────────
DEMOTE_ENDPOINT = '''

@bp.route("/api/students/demote-bulk", methods=["POST"])
@token_required
def demote_students_bulk(current_user):
    """
    Bulk DEMOTE (de-promote) students — reverting a mistaken promotion.

    ERP-safe: Uses state transitions, never deletes data.
    - Fee structures in source_year are deactivated (not deleted).
    - Real payment transactions are NEVER touched (audit trail).
    - The source_year academic record is preserved but cleared of is_promoted flag.
    - Student pointer (academic_year, clazz, section) is restored to restore_year.

    Request body:
        student_ids  : list[int]
        source_year  : str  — the year the student was MISTAKENLY promoted TO
        restore_year : str  — the year the student should be RESTORED to
    """
    data = request.json or {}
    student_ids = data.get("student_ids", [])
    source_year = data.get("source_year")      # wrong promoted year (FROM)
    restore_year = data.get("restore_year")    # correct year to go back TO

    if not isinstance(student_ids, list) or not student_ids:
        return jsonify({"error": "student_ids must be a non-empty list"}), 400
    if not source_year or not restore_year:
        return jsonify({"error": "source_year and restore_year are required"}), 400
    if source_year == restore_year:
        return jsonify({"error": "source_year and restore_year cannot be the same"}), 400

    success_count = 0
    errors = []
    processed_ids = set()

    try:
        students = Student.query.filter(Student.student_id.in_(student_ids)).all()
        student_map = {s.student_id: s for s in students}

        if not_found := [sid for sid in student_ids if sid not in student_map]:
            errors.append(f"Students not found: {', '.join(map(str, not_found))}")

        if current_user.role != "Admin" and current_user.branch != "All":
            for sid in list(student_map.keys()):
                if student_map[sid].branch != current_user.branch:
                    errors.append(f"Unauthorized for student {student_map[sid].admission_no}")
                    del student_map[sid]

        for student_id, student in student_map.items():
            if student_id in processed_ids:
                continue
            processed_ids.add(student_id)

            try:
                # 1. Verify the source year record exists (the mistakenly promoted year)
                source_record = StudentAcademicRecord.query.filter_by(
                    student_id=student_id, academic_year=source_year
                ).first()
                if not source_record:
                    errors.append(
                        f"{student.admission_no}: No record found for source year {source_year}."
                    )
                    continue

                # 2. Verify the restore year record exists
                restore_record = StudentAcademicRecord.query.filter_by(
                    student_id=student_id, academic_year=restore_year
                ).first()
                if not restore_record:
                    errors.append(
                        f"{student.admission_no}: No record found for restore year {restore_year}. "
                        "Student may not have belonged to that year."
                    )
                    continue

                # 3. Soft-deactivate data tied to the mistaken source year
                _deactivate_student_year_data(
                    student_id, source_year, demoted_by_user_id=current_user.user_id
                )

                # 4. Clear is_promoted on source record (keep row for audit)
                source_record.is_promoted = False
                source_record.promoted_date = None

                # 5. Reactivate restore year record (student is back here)
                restore_record.is_promoted = False

                # 6. Point the Student back to restore year
                student.academic_year = restore_year
                student.clazz = restore_record.class_name
                student.section = restore_record.section
                student.Roll_Number = restore_record.roll_number

                db.session.commit()
                success_count += 1
                logger.info(
                    "Demoted student %s from %s to %s by user %s",
                    student.admission_no, source_year, restore_year, current_user.username
                )

            except Exception as e:
                db.session.rollback()
                errors.append(f"Error demoting {student.admission_no}: {str(e)}")
                logger.error("Demotion error for %s: %s", student.admission_no, e, exc_info=True)

        return jsonify({
            "message": f"Demotion complete. {success_count} student(s) successfully demoted.",
            "success_count": success_count,
            "errors": errors
        }), 200 if success_count > 0 else 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

'''

SUMMARY_ROUTE = '@bp.route("/api/students/summary", methods=["GET"])'
if SUMMARY_ROUTE in content_lf:
    content_lf = content_lf.replace(SUMMARY_ROUTE, DEMOTE_ENDPOINT + SUMMARY_ROUTE, 1)
    print("Injected demote-bulk endpoint")
else:
    print("WARNING: Could not find summary route anchor, appending at end")
    content_lf += DEMOTE_ENDPOINT

# ── 4. Write back ────────────────────────────────────────────────────────────
with open(ROUTES_FILE, "w", encoding="utf-8", newline="\r\n") as f:
    f.write(content_lf)
print("File written successfully.")
