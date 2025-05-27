def num_of_words(text):
    words = text.split()
    cnt = 0
    for word in words:
        cnt += 1
    print(f'{cnt} words found in the document')

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    franken_path = './books/frankenstein.txt'
    franken_text = get_book_text(franken_path)
    print(franken_text)
    num_of_words(franken_text)

main()
