# Лаба 8

Класс

```py

DATE_FMT = "%Y-%m-%d"


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        if not self.fio or not isinstance(self.fio, str):
            raise ValueError("ФИО обязательно и должно быть строкой")

        try:
            datetime.strptime(self.birthdate, DATE_FMT)
        except ValueError:
            raise ValueError(
                f"Дата рождения обязательна и должна быть в формате: {DATE_FMT}"
            )

        if not self.group or not isinstance(self.group, str):
            raise ValueError("Группа обязательна и должна быть строкой")

        if not isinstance(self.gpa, (float, int)):
            raise ValueError("Средний балл обязателен и должен быть числом")

        if not (0 <= float(self.gpa) <= 5):
            raise ValueError("Средний балл должен быть 0 <= и <= 5")

        self.gpa = float(self.gpa)

    def age(self) -> int:
        b = datetime.strptime(self.birthdate, DATE_FMT).date()
        today = date.today()
        full_years = today.year - b.year - ((today.month, today.day) < (b.month, b.day))
        return full_years

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        if not isinstance(data, dict):
            raise ValueError("Данные должны быть dict")

        required = {"fio", "birthdate", "group", "gpa"}
        missing = required - data.keys()
        if missing:
            raise ValueError(f"Лишние данные: {missing}")

        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"],
        )

    def __str__(self):
        return f"{self.fio} ({self.group}), GPA={self.gpa}, age={self.age()}"

```

Сериализаторы

```py
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

```

Запуск

```py
def main():
    students = [
        Student(
            fio="Межеровская Анна Сергеевна",
            birthdate="2007-11-04",
            group="BIVT-25-4",
            gpa=0.01,
        ),
        Student(
            fio="Кабанова Амалия Сергеевна",
            birthdate="2009-01-18",
            group="BIVT-25-4",
            gpa=5.0,
        ),
        Student(
            fio="Муфазалов Эрик Мансурович",
            birthdate="2007-08-28",
            group="BIVT-25-4",
            gpa=5.0,
        ),
    ]

    json_path = Path("src/lab08/data/students.json")

    students_to_json(students, json_path)
    print(f"→ JSON сохранён в {json_path}")

    loaded_students = students_from_json(json_path)
    print("→ Загружено студентов:", len(loaded_students))

    print("\nСтуденты из JSON")
    for s in loaded_students:
        print(s)
        print()


if __name__ == "__main__":
    main()
```

Вывод в консоль

![Вывод](./images/main.png)

Вывод в файл

![Вывод](./images/file.png)
