import sys

from lib.text import normalize, tokenize, count_freq, top_n


def main():
    text = sys.stdin.read().strip()

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")

    if top_words:
        max_word_len = max(len(word) for word, _ in top_words)
        col_width = max(max_word_len, 10)

        print(f"\n{'слово':<{col_width}} | частота")
        print("-" * col_width + "-|--------")

        for word, count in top_words:
            print(f"{word:<{col_width}} | {count}")


if __name__ == "__main__":
    main()
