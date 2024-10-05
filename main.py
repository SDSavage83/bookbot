def main():
    file = "books/frankenstein.txt"
    output_of_file = output_complete_file(file)
    wordcount_of_file = count_words(output_of_file)
    character_count_dictionary = count_characters(output_of_file)
    list_of_dict = create_list_of_dictionaries(character_count_dictionary)
    list_of_dict.sort(reverse=True, key=sort_on)
    #print(output_of_file)
    #print(wordcount_of_file)
    #print(character_count)
    generate_report(wordcount_of_file, list_of_dict, file)

def split_to_list(file):
    return file.split()

def count_words(file):
    length_of_list = len(split_to_list(file))
    return length_of_list

def output_complete_file(book):
    with open(book) as f:
        file_output = f.read()
    return file_output

def count_characters(file):
    char_count_dict = {}
    #for item in range(0, 5):
    for item in split_to_list(file):
        #lowered = item.lower()
        #print(lowered)
        for char in item.lower():
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
    return char_count_dict

def create_list_of_dictionaries(char_dict):
    list_of_dict = []
    for char in char_dict:
        count = char_dict[char]
        #print(f"Letter: {char}, Count: {count}")
        if char.isalpha() == True:
            list_of_dict.append({"letter": char, "count": count})
    return list_of_dict

def sort_on(dict):
    return dict["count"]



def generate_report(wordcount, list_of_dict, file):
    print(f"--- Begin report of {file} ---")
    print(f"{wordcount} words found in the document")
    print()
    for dict in list_of_dict:
        print(f"The '{dict['letter']}' character was found {dict['count']} times")
    print("--- End report ---")
    
    
main()