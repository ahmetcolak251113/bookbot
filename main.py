# main.py
import sys
from stats import get_book_text, get_num_words, count_chars, chars_to_sorted_list

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 
path = sys.argv[1]
print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")

text = get_book_text(path)
total_words = get_num_words(text)
print(f"Found {total_words} total words")

print("--------- Character Count -------")
char_counts = count_chars(text)
sorted_chars = chars_to_sorted_list(char_counts)

for item in sorted_chars:
    ch = item["char"]
    if not ch.isalpha():
        continue
    print(f"{ch}: {item['num']}")

print("============= END ===============")


