# Лаба 4

Задача A

```py
from pathlib import Path
import csv


def read_text(path, encoding="utf-8"):
    path = Path(path)

    with open(path, "r", encoding=encoding) as file:
        return file.read()


def write_csv(
    rows,
    path,
    header=None,
):
    path = Path(path)

    if rows:
        first_length = len(rows[0])
        for row in rows:
            if len(row) != first_length:
                raise ValueError(
                    f"Строка имеет длину {len(row)}, ожидалось {first_length}"
                )

    if header:
        if len(header) != len(rows[0]):
            raise ValueError(
                f"Заголовок имеет длину {len(header)}, а строки - {len(rows[0])}"
            )

    ensure_parent_dir(path)

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")

        if header:
            writer.writerow(header)

        writer.writerows(rows)


def ensure_parent_dir(path):
    path = Path(path)
    parent_dir = path.parent
    parent_dir.mkdir(parents=True, exist_ok=True)


try:
    content = read_text("src/lab04/data/input.txt", encoding="utf-8")
    print(content)
except FileNotFoundError:
    print("FileNotFoundError: Файл не найден")
except UnicodeDecodeError:
    print("UnicodeDecodeError: Ошибка кодировки")

write_csv([("test", 3), ("test2", 4)], "src/lab04/data/check.csv", header=("word", "count"))
```

Результат работы [```text_report.py```](./src/text_report.py)

![Результат работы](./images/text_report.png)

Входной файл [```input.txt```](./data/input.txt)

![Входной файл](./images/in_text_report.png)

Выходной [```report.csv```](./data/report.csv)

![Выходной файл](./images/out_text_report.png)

Задача B

```py
from pathlib import Path
import csv

from lib.text import normalize, tokenize, count_freq, top_n


def read_input_file(path):
    path = Path(path)

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_report_csv(frequencies, path):
    path = Path(path)
    sorted_items = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))

    with open(path, "w", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")

        writer.writerow(("word", "count"))

        writer.writerows(sorted_items)


def print_summary(tokens, frequencies, top_n):
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print("Топ-5:")

    for item in top_n:
        print(f"{item[0]}: {item[1]}")


if __name__ == "__main__":
    input_path = "src/lab04/data/input.txt"
    output_path = "src/lab04/data/report.csv"

    try:
        text = read_input_file(input_path)

        normalized_text = normalize(text)
        tokens = tokenize(normalized_text)
        frequencies = count_freq(tokens)
        top_5 = top_n(frequencies, 5)

        write_report_csv(frequencies, output_path)

        print_summary(tokens, frequencies, top_5)

    except FileNotFoundError:
        print("Убедитесь, что файл data/input.txt существует")
```

Результат работы [```oi_txt_csv.py```](./src/io_txt_csv.py)

![Результат работы](./images/io_txt_csv.png)

Входной файл [```input.txt```](./data/input.txt)

![Входной файл](./images/in_text_report.png)

Выходной [```check.csv```](./data/check.csv)

![Выходной файл](./images/out_io_txt_csv.png)
