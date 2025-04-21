import sys
def get_book_text():
    with open(file_path) as f:
        # this opens the file defined in the path and gives it a new name 'f'
        file_contents = f.read()
        # this converts file contents into a string.
    # print(file_contents)
    return file_contents
        # returns file contents as one continuous string.

def word_count(text):
    word_list = text.split()
    word_count = len(word_list)
    #print(f"{word_count} words found in the document")
    return word_count

def char_count(text):
    letters_dict = {}
    lower_case = text.lower()
    for char in lower_case:
        if char in letters_dict:
            letters_dict[char] += 1
        else:
            letters_dict[char] = 1
    #print(letters_dict)
    return letters_dict

def sorted_characters(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    
    def sort_on(dict_items):
        return dict_items["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def filepath():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        print(f"{sys.argv[1]}")
        return file_path
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

file_path = filepath()