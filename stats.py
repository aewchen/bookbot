def get_num_words(content):
  words = content.split()
  number_of_words = len(words)
  return number_of_words

def get_characters_dict(content):
  characters = {}
  words = content.split()

  for word in words:
    for char in word:
      char = char.lower()

      if char in characters.keys():
        characters[char] = characters[char] + 1
      else:
        characters[char] = 1
  return characters


