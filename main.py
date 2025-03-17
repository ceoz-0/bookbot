from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        content = f.read()

    return content

def main():
    book_string = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book_string)
    print(f"{num_words} words found in the document")



main()
