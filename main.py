def main():
    file = "books/frankenstein.txt"
    file_contents = split_words_into_list(file)
    count_words(file_contents)
    print(file_contents)
    print(count_words(file_contents))

def count_words(list):
    all_the_words = list.split()
    count_of_words = len(all_the_words)
    return count_of_words

def split_words_into_list(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents
    
main()