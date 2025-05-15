from stats import count_all_the_words
from stats import count_all_the_Letters
from stats import list_of_dictionaries
import sys


def get_book_text(path_of_file):
    with open(path_of_file) as f:
        file_contents = f.read()


    return file_contents

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]

    text_of_book = get_book_text(path_to_book)
#    print(text_of_book)
    number_of_words = count_all_the_words(text_of_book)
#    print(number_of_words,"words found in the document")
    dictionary_of_letters = count_all_the_Letters(text_of_book)
#    print(dictionary_of_letters)
    
    sorted_list = list_of_dictionaries(dictionary_of_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print("Found", number_of_words, "total words")
    print("--------- Character Count -------")
#    print(sorted_list)
    for item in sorted_list:
    #    print(item["char"])
        if item["char"].isalpha():
            char_to_print = item["char"]
            num_to_print = item["num"]
            print(f"{char_to_print}: {num_to_print}")
            #print(item["char"], item["num"])
    print("============= END ===============")


main()