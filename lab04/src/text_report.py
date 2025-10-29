import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from lib.text import normalize, tokenize, count_freq, top_n


def read_input_file(file_path):
    if not file_path.exists():
        raise FileNotFoundError(f"Входной файл не найден: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_report_csv(frequencies, output_path):
    sorted_items = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("word,count\n")

        for word, count in sorted_items:
            file.write(f"{word},{count}\n")


def print_summary(tokens, frequencies, top_n):
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print("Топ-5:")

    for word, count in (top_n, 1):
        print(f"{word}: {count}")


def main():
    input_path = Path("lab04/data/input.txt")
    output_path = Path("lab04/data/report.csv")

    try:
        text = read_input_file(input_path)

        normalized_text = normalize(text)
        tokens = tokenize(normalized_text)
        frequencies = count_freq(tokens)
        top_5 = top_n(frequencies, 5)

        write_report_csv(frequencies, output_path)

        print_summary(tokens, frequencies, top_5)

    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        print("Убедитесь, что файл data/input.txt существует")
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
