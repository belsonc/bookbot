def count_all_the_words(book_to_count):
    individual_words = book_to_count.split()
    return len(individual_words)

def count_all_the_Letters(book_to_count):
    dictionary_of_characters = {}
    #for each character, convert it to lowercase, check if it's in the dictionary, if it is, add 1 to the value, if it's not, add it
#    lowercase_book = book_to_count.lower()
#    print(lowercase_book)

    for x in range(0,len(book_to_count)):
        lowercase_letter = book_to_count[x].lower()
        if lowercase_letter in dictionary_of_characters:
            dictionary_of_characters[lowercase_letter] += 1
        else:
            dictionary_of_characters[lowercase_letter] = 1

#    for x in range(0, len(lowercase_book)):
 #       if lowercase_book[x] not in dictionary_of_characters:
  #          dictionary_of_characters[book_to_count[x]] = 1
   #     else:
    #        dictionary_of_characters[book_to_count[x]] += 1

    return dictionary_of_characters

def sort_on(dict):
    return dict["num"]

def list_of_dictionaries(letters_and_count):
    list_of_letters = []
    for letter in letters_and_count:
        temp_dictionary = {"char": letter, "num": letters_and_count[letter]}
        list_of_letters.append(temp_dictionary)
    list_of_letters.sort(reverse=True, key=sort_on)
    
    return list_of_letters

