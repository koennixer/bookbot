def get_num_words(book):
    """Returns the number of words in a string"""
    return len(book.split())

def get_letter_count(book):
    """Returns the number of letters in a string"""
    letters = {}
    for letter in book.lower():
        if letter.isalpha():
            if letter in letters:
                letters[letter] = letters[letter] + 1
            else:
                letters[letter] = 1
    return letters

def sort_count(count):
    """Sorts the dicitionary of the lettercount"""
    sorted_letter = {}
    for key in sorted(count, reverse=True, key=count.get):
        sorted_letter[key] = count[key]
    return sorted_letter