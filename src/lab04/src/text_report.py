import csv
from pathlib import Path

from src.lib.text import count_freq, normalize, tokenize, top_n


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
    input_path = "src/src/lab04/data/input.txt"
    output_path = "src/src/lab04/data/report.csv"

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
