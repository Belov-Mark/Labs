import sys
import os
sys.path.insert(0, '/home/mark/Labs')

from lib.text import normalize, tokenize, count_freq, top_n


TABLE_MODE = os.getenv('TEXT_STATS_TABLE', '0') == '1'

def main():
    text = sys.stdin.read().strip()
    
    if not text:
        print("Всего слов: 0")
        print("Уникальных слов: 0")
        print("Топ-5:")
        return
    
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)
    
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    
    if TABLE_MODE and top_words:
        max_word_len = max(len(word) for word, _ in top_words)
        col_width = max(max_word_len, 6)
        
        print("\nслово".ljust(col_width) + " | частота")
        print("-" * col_width + "-|--------")
        
        for word, count in top_words:
            print(word.ljust(col_width) + f" | {count}")
    else:
        print("Топ-5:")
        for word, count in top_words:
            print(f"{word}:{count}")

