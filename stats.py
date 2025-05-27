def num_of_words(text):
    words = text.split()
    cnt = 0

    for word in words:
        cnt += 1

    print(f'{cnt} words found in the document')

def get_duplicates(text):
    words = text.lower()
    duplicates = {}

    for character in words:
        if character in duplicates:
            duplicates[character] += 1
        else:
            duplicates[character] = 1

    return duplicates
