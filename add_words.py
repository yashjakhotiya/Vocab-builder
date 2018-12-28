#!/usr/bin/env python3
import json, os

# global path variable for the dictionary

path = "./dictionary.json"

def main():

	_dict = {}
	new_dict = {}
	
	if os.path.isfile(path):
		with open(path, 'rt') as fp:
			_dict = json.load(fp)

	print("\nEnter the word first, then the definition and then the example.\nEnter q in any place to abort.")
	
	while True:
		print("\nWord :", end=' ')
		word = input()
		if word == 'q':
			break

		if word in _dict.keys() or word in new_dict:
			print("Word already exists in your dictionary. Enter s to skip this word, any other key to continue :", end=' ')
			cmnd = input()
			if cmnd == 's':
				continue

		print("Definition :", end=' ')
		defn = input()
		if defn == 'q':
			break

		print("Example :", end=' ')
		example = input()
		if example == 'q':
			break

		new_dict.update({word:(defn, example)})

	_dict.update(new_dict)
	
	with open(path, 'wt') as fp:
		json.dump(_dict, fp)
		if new_dict != {}:
			print("Words successfully added to the dictionary")
			print("Current word count in your dictionary - {}".format(len(_dict)))

if __name__ == '__main__':
	main()