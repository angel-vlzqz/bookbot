def num_of_words(text):
    words = text.split()
    cnt = 0

    for word in words:
        cnt += 1

    print(f'{cnt} words found in the document')
    return cnt

def get_duplicates(text):
    words = text.lower()
    duplicates = {}

    for character in words:
        if character in duplicates:
            duplicates[character] += 1
        else:
            duplicates[character] = 1

    return duplicates

def sort_on(dict):
    return dict['num']

def print_report(path, word_count, characters):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    # characters.sort(reverse=True, key=sort_on)
    for character in characters:
        if character.isalpha() == True:
            print(f'{character}: {characters[character]}')
