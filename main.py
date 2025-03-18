from stats import get_num_words
from stats import count_chars
from stats import dict_sorter
import sys
def get_book_text(path):
    with open(path) as f:
        content = f.read()

    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_string = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    num_words = get_num_words(book_string)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_dict = count_chars(book_string)
    print("--------- Character Count -------")
    dict_sorter(char_dict)

main()
