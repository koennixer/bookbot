import sys
from stats import get_num_words, get_letter_count, sort_count

def get_book_text(path):
    """Returns the file found at path as a string"""
    book = ""
    with open(path) as f:
        book = f.read()
    return book

def main():
    if len(sys.argv) != 2:
        print("Wrong input")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    count = sort_count(get_letter_count(book))
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path}')
    print("----------- Word Count ----------")
    print(f'Found {get_num_words(book)} total words')
    print("--------- Character Count -------")
    for key, value in count.items():
        print(f'{key}: {value}')
    print("============= END ===============")

main()