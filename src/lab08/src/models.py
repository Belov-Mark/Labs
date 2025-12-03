from dataclasses import dataclass
from datetime import date, datetime

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
