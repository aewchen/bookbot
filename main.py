from stats import get_num_words, get_characters_dict
def get_book_text(filepath):
	file_contents = None
	with open(filepath) as f:
		file_contents = f.read()

	return file_contents

#def get_num_words(content):
#	words = content.split()
#	number_of_words = len(words)
#	return number_of_words

def main():
	filepath = "books/frankenstein.txt"
	content = get_book_text(filepath)
	#print(content)
	
	num = get_num_words(content)
	print(f"{num} words found in the document")

	characters = get_characters_dict(content)
	print(characters)

main()
