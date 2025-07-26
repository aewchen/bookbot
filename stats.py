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

def get_sorted_list(characters):
  #sorted_dict = characters.sort(reverse=True, key= lambda x: x[
  sorted_list = sorted(characters.items(), reverse=True, key=lambda item: item[1])
  filtered_string_list = [ f"{values[0]}: {values[1]}" for values in sorted_list if values[0].isalpha()]
  final_string = "\n".join(filtered_string_list)
  return final_string
