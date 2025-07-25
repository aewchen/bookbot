#!/bin/python3
from stats import get_num_words, get_characters_dict, get_sorted_list
import sys

def get_book_text(filepath):
  file_contents = None
  with open(filepath) as f:
    file_contents = f.read()

  return file_contents

#def get_num_words(content):
# words = content.split()
# number_of_words = len(words)
# return number_of_words

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  filepath = sys.argv[1]
  content = get_book_text(filepath)
  #print(content)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  num = get_num_words(content)
  print(f"Found {num} total words")
  print("--------- Character Count -------")
  characters = get_characters_dict(content)
  print(get_sorted_list(characters))
  print("============= END ===============")
main()
