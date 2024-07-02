def main():
    file_path = "books/frankenstein.txt"
    with open(f"{file_path}") as f:
        file_contents = f.read()
        
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)
        character_dicts = create_character_dicts(character_count)
        print_book_report(file_path, word_count, character_dicts)
        
def count_words(input_string):
    words = input_string.split()
    return len(words)

def count_characters(input_string):
    per_character_count = {}
    lower_case_input_string = input_string.lower()
    for character in lower_case_input_string:
        if character in per_character_count:
            per_character_count[character] +=1
        else:
            per_character_count[character] = 1
    return per_character_count

def print_book_report(path_to_file, word_count, character_dicts):
    print(f"--- Begin report of {path_to_file} ---")
    print()
    print(f"{word_count} words found in the document")
    for char in character_dicts:
        print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End report ---")

def create_character_dicts(character_count):
    list_of_dicts = []
    for char in character_count:
        if char.isalpha():
            new_dict = {
                'char': char,
                'num': character_count[char]
            }
            list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=lambda dict: dict['num'])
    return list_of_dicts

main()