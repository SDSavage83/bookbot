def main():
    file = "books/frankenstein.txt"
    output_of_file = output_complete_file(file)
    wordcount_of_file = count_words(output_of_file)
    character_count = count_characters(output_of_file)
    #print(output_of_file)
    print(wordcount_of_file)
    print(character_count)

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

main()