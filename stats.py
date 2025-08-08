# stats.py

def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def get_num_words(text: str) -> int:
    return len(text.split())

def count_chars(text: str) -> dict[str, int]:
    text = text.lower()
    counts: dict[str, int] = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def chars_to_sorted_list(char_counts: dict[str, int]) -> list[dict]:
    items = [{"char": ch, "num": n} for ch, n in char_counts.items()]
    items.sort(key=lambda d: d["num"], reverse=True)
    return items
