from stats import get_word_count, get_letter_count

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    
    count = get_word_count(text)
    print(f'Found {count} total words')
    
    char_count = get_letter_count(text)
    print(char_count)

main()
