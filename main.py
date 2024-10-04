def main():
    file = "books/frankenstein.txt"
    output_of_file = output_complete_file(file)
    wordcount_of_file = count_words(output_of_file)
    print(output_of_file)
    print(wordcount_of_file)

def count_words(list):
    file_as_list = list.split()
    length_of_list = len(file_as_list)
    return length_of_list

def output_complete_file(book):
    with open(book) as f:
        file_output = f.read()
    return file_output
    
main()