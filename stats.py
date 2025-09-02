#python

def get_num_words(file):
  word_count = file.split()
  return len(word_count)

def get_num_characters(file):
  lower_file = file.lower()
  character_count = {}
  for character in lower_file:
    character_count[character] = character_count.get(character, 0) + 1
  return character_count

def sort_value(character_dict):
  return character_dict["num"]

def character_dict_to_sorted_list(num_chars_dict):
  sorted_list = []
  for character in num_chars_dict:
    if character.isalpha():
      sorted_list.append({"char": character, "num": num_chars_dict[character]})
  sorted_list.sort(reverse=True, key=sort_value)
  return sorted_list

