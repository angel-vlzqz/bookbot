from stats import num_of_words, get_duplicates, print_report

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    franken_path = './books/frankenstein.txt'
    franken_text = get_book_text(franken_path)
    franken_duplicates = get_duplicates(franken_text)
    franken_num_of_words = num_of_words(franken_text)
    print_report(franken_path, franken_num_of_words, franken_duplicates)



main()
