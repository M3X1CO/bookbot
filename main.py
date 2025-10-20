import sys

from stats import get_word_count, get_letter_count, get_sorted

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    
    count = get_word_count(text)    
    char_count = get_letter_count(text)
    sort_chars = get_sorted(char_count)
    
    #print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sort_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
