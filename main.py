def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    counted = count_chars(text)
    words = word_count(text)

    sorted = sort_dict(counted)
    print(f"{words} words found in the document")
    for item in sorted:
        print(f"The '{item['character']}' character was found {item['count']} times")


def word_count(text):
    return len(text.split())

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    list = []
    for k in dict:
        if k.isalpha():
            list.append({ "character": k, "count": dict[k]})

    list.sort(reverse=True, key=sort_on)
    return list

def count_chars(text):
    char_dict = {}

    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
