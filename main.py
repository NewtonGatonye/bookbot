import sys
from stats import get_book_text, word_count, char_count, sorted_characters, filepath

def main():
    
    file_path = filepath()
    # Get the text
    text = get_book_text()
    
    # Get word count
    total_words = word_count(text)
    
    # Get character counts
    char_counts = char_count(text)
    
    # Get sorted character list
    sorted_chars = sorted_characters(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    # Print each character count (only alphabetical characters)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
