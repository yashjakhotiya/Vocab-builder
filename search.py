#!/usr/bin/env python3
import json, os, sys

# global path variable for the dictionary

path = "./dictionary.json"

def main():
	
	if os.path.isfile(path):
		with open(path, 'rt') as fp:
			_dict = json.load(fp)
		print("\nDictionary loaded successfully with word count of {}".format(len(_dict)))
	
	else:
		print("\nDictionary file not found.\nPlease copy a file or use the add_words program.\n")
		sys.exit(-1)

	print("\nEnter the word to be searched")
	print("OR l to list all words, ld to list all words with definitons and examples, q to quit")
		
	while True:

		print("\nWord :", end=' ')	
		word = input()

		if word == 'l':
			print()
			for key in sorted(_dict):
				print(key)

		elif word == 'ld':
			for key in sorted(_dict):
				defn, example = _dict[key]
				print("\nWord : {}".format(key))
				print("Definition : {}".format(defn))
				print("Example : {}".format(example))

		elif word == 'q':
			break

		elif word in _dict:
			defn, example = _dict[word]
			print("Definition : {}".format(defn))
			print("Example : {}".format(example))

		else:
			print("'{}' not found in your custom dictionary, add it using the add_words program.".format(word))
		
if __name__ == '__main__':
	main()