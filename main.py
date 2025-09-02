
# python
import sys

from stats import get_num_words
from stats import get_num_characters
from stats import character_dict_to_sorted_list

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def sorted_list_to_dict():
  sorted_character_dict = {}

def main():
  argument = sys.argv
  if len(sys.argv) != 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

  text = get_book_text(argument[1])
  word_count = get_num_words(text)
  character_count = get_num_characters(text)
#  print(f"{word_count} words found in the document")
  sorted_list = character_dict_to_sorted_list(character_count)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {argument[1]}...")
  print(" ---------- Word Count ---------- ")
  print(f"Found {word_count} total words")
  print(" ---------- Character Count ----------")
  for character_dict in sorted_list:
    print(f'{character_dict["char"]}: {character_dict["num"]}')


if __name__ == "__main__":
  main()
