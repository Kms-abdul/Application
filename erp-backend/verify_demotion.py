with open(r'd:\E drive\Development\Projects\HIFZ ERP\MS Hifz Scientifc study Programm\HifzErpSoftwareApplication\frontend\src\components\StudentAdministration.tsx', 'r', encoding='utf-8') as f:
    c = f.read()

checks = [
    ('DemoteStudents import', "import DemoteStudents from './DemoteStudents'" in c),
    ("demote in view type", "'demote'" in c),
    ('De-promote nav button', 'De-promote' in c),
    ('demote case in switch', "case 'demote':" in c),
    ('DemoteStudents component used', '<DemoteStudents' in c),
]
for name, ok in checks:
    print('  [' + ('OK' if ok else 'FAIL') + '] ' + name)

with open(r'd:\E drive\Development\Projects\HIFZ ERP\MS Hifz Scientifc study Programm\HifzErpSoftwareApplication\erp-backend\routes\student_routes.py', 'r', encoding='utf-8') as f:
    c2 = f.read()

backend_checks = [
    ('_deactivate_student_year_data exists', '_deactivate_student_year_data' in c2),
    ('_purge_student_year_data removed', '_purge_student_year_data' not in c2),
    ('demote-bulk route', 'demote-bulk' in c2),
    ('demote_students_bulk function', 'def demote_students_bulk' in c2),
]
print()
for name, ok in backend_checks:
    print('  [' + ('OK' if ok else 'FAIL') + '] ' + name)
