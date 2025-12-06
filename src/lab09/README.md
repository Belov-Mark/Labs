# Лаба 9

Класс

```py
CSV_HEADER = ["fio", "birthdate", "group", "gpa"]


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists():
            with self.path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(CSV_HEADER)

    def _read_all(self) -> list[Student]:
        self._ensure_storage_exists()

        with self.path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if reader.fieldnames != CSV_HEADER:
                raise ValueError("Некорректный заголовок CSV")

            students = []
            for row in reader:
                try:
                    students.append(
                        Student(
                            fio=row["fio"],
                            birthdate=row["birthdate"],
                            group=row["group"],
                            gpa=float(row["gpa"]),
                        )
                    )
                except Exception as e:
                    raise ValueError(f"Некорректная строка CSV: {row}") from e

            return students

    def _write_all(self, students: list[Student]):
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
            writer.writeheader()
            for s in students:
                writer.writerow(
                    {
                        "fio": s.fio,
                        "birthdate": s.birthdate,
                        "group": s.group,
                        "gpa": s.gpa,
                    }
                )

    def get_list(self) -> list[Student]:
        return self._read_all()

    def add(self, student: Student):
        with self.path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
            writer.writerow(
                {
                    "fio": student.fio,
                    "birthdate": student.birthdate,
                    "group": student.group,
                    "gpa": student.gpa,
                }
            )

    def find(self, substr: str) -> list[Student]:
        substr = substr.lower()
        students = self._read_all()
        return [s for s in students if substr in s.fio.lower()]

    def remove(self, fio: str):
        students = self._read_all()
        students = [s for s in students if s.fio != fio]
        self._write_all(students)

    def update(self, fio: str, **fields):
        students = self._read_all()
        updated = False

        for i, s in enumerate(students):
            if s.fio == fio:
                data = {
                    "fio": fields.get("fio", s.fio),
                    "birthdate": fields.get("birthdate", s.birthdate),
                    "group": fields.get("group", s.group),
                    "gpa": float(fields.get("gpa", s.gpa)),
                }
                students[i] = Student(**data)
                updated = True

        if not updated:
            raise ValueError(f"Студент '{fio}' не найден")

        self._write_all(students)

    def stats(self) -> dict:
        students = self._read_all()
        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": [],
            }

        gpas = [s.gpa for s in students]

        groups: dict[str, int] = {}
        for s in students:
            groups[s.group] = groups.get(s.group, 0) + 1

        top5 = sorted(students, key=lambda s: s.gpa, reverse=True)[:5]
        top5 = [{"fio": s.fio, "gpa": s.gpa} for s in top5]

        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": sum(gpas) / len(gpas),
            "groups": groups,
            "top_5_students": top5,
        }
```

Тесты
![Вывод](./images/tests.png)
