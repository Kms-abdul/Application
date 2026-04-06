import sys

FILE = r"d:\E drive\Development\Projects\HIFZ ERP\MS Hifz Scientifc study Programm\HifzErpSoftwareApplication\frontend\src\components\StudentAdministration.tsx"

with open(FILE, "r", encoding="utf-8") as f:
    src = f.read()

# ── 1. Add DemoteStudents import after PromoteStudents ──
src = src.replace(
    "import PromoteStudents from './PromoteStudents';",
    "import PromoteStudents from './PromoteStudents';\nimport DemoteStudents from './DemoteStudents';"
)

# ── 2. Add 'demote' to StudentAdminView union type ──
src = src.replace(
    "type StudentAdminView =\n    'students' | 'search' | 'summary' | 'reports' | 'certificates' | 'upgrade'\n    | 'import' | 'addStudent' | 'viewStudent' | 'editStudent'\n    | 'inactive' | 'inactiveReport';",
    "type StudentAdminView =\n    'students' | 'search' | 'summary' | 'reports' | 'certificates' | 'upgrade'\n    | 'import' | 'addStudent' | 'viewStudent' | 'editStudent'\n    | 'inactive' | 'inactiveReport' | 'demote';"
)

# ── 3. Add Demote button next to Upgrade button in nav ──
src = src.replace(
    "                        <button className={btn('upgrade')} onClick={() => setActiveView('upgrade')}>Upgrade</button>",
    "                        <button className={btn('upgrade')} onClick={() => setActiveView('upgrade')}>Upgrade</button>\n                        <button className={btn('demote')} onClick={() => setActiveView('demote')}>De-promote</button>"
)

# ── 4. Add case 'demote' to the switch statement ──
src = src.replace(
    "            case 'upgrade':\n                return <PromoteStudents onBack={() => setActiveView('students')} />;",
    "            case 'upgrade':\n                return <PromoteStudents onBack={() => setActiveView('students')} />;\n\n            case 'demote':\n                return <DemoteStudents onBack={() => setActiveView('students')} />;"
)

with open(FILE, "w", encoding="utf-8", newline="\r\n") as f:
    f.write(src)

print("StudentAdministration.tsx patched successfully.")
