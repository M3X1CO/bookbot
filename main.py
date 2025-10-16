def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()




def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(text)



main()
