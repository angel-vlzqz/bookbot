from stats import num_of_words, get_duplicates

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    franken_path = './books/frankenstein.txt'
    franken_text = get_book_text(franken_path)
    franken_duplicates = get_duplicates(franken_text)
    print(franken_text)
    num_of_words(franken_text)
    print(franken_duplicates)

main()
