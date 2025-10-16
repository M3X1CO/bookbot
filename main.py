def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def get_word_count(verse):
    word_count = verse.split()
    return len(word_count)


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    count = get_word_count(text)

    print(f'Found {count} total words')

main()
