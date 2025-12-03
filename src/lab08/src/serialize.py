import json
from pathlib import Path

from models import Student


def students_to_json(students: list[Student], path: str | Path) -> None:
    path = Path(path)

    data = [s.to_dict() for s in students]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> list[Student]:
    path = Path(path)

    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    if not isinstance(raw, list):
        raise ValueError("JSON must contain array of students")

    students = []
    for obj in raw:
        try:
            student = Student.from_dict(obj)
            students.append(student)
        except Exception as e:
            raise ValueError(f"invalid student object: {obj!r}, error: {e}") from e

    return students
