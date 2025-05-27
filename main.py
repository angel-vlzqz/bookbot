from stats import num_of_words, get_duplicates, print_report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    franken_path = sys.argv[1]
    franken_text = get_book_text(franken_path)
    franken_duplicates = get_duplicates(franken_text)
    franken_num_of_words = num_of_words(franken_text)
    print_report(franken_path, franken_num_of_words, franken_duplicates)



main()
