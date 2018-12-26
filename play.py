#!/usr/bin/env python3
import json, os, sys, random

# global path variable for the dictionary

path = "./dictionary.json"

# number alphabet mapping

choice_map = {0:'a', 1:'b', 2:'c', 3:'d'}

def main():
	
	if os.path.isfile(path):
		with open(path, 'rt') as fp:
			_dict = json.load(fp)
		print("\nDictionary loaded successfully with word count of {}\n".format(len(_dict)))
	
	else:
		print("\nDictionary file not found.\nPlease copy a file or use the add_words program.\n")
		sys.exit(-1)

	print("Enter the number of words you wish to test in this game, for example 5, 10 or 25 -", end=' ')
	game_count = int(input())
	dict_count = len(_dict)

	if game_count <= dict_count:
		keys = random.sample(list(_dict.keys()), game_count)
	else:
		keys = []
		for x in range(game_count//dict_count):
			keys += random.sample(list(_dict.keys()), dict_count)
		keys += random.sample(list(_dict.keys()), game_count - (game_count//dict_count)*dict_count)

	print("\nFor each of the following words, enter the choice which most accurately matches its definition")
	
	correct_ans_count = 0
	for x, key in enumerate(keys):
		print("\n{}. Word - '{}'\n".format(x+1, key))
		
		defn, example = _dict[key]
		wrong_defns_examples = list(_dict.values())
		wrong_defns_examples.remove([defn, example])
		if dict_count < 4:
			wrong_defns_examples = random.choices(wrong_defns_examples, k=3)
		else:
			wrong_defns_examples = random.sample(wrong_defns_examples, k=3)
		wrong_defns = []
		for i in range(3):
			wrong_defns += [wrong_defns_examples[i][0]]
		choices =  [defn] + wrong_defns
		random.shuffle(choices)
		for i, choice in enumerate(choices):
			print("{}. {}".format(choice_map[i], choice))

		correct_choice = choices.index(defn)
		correct_choice = choice_map[correct_choice]

		print("\nAnswer -", end=' ')
		ans = input()
		if ans == correct_choice:
			print("\nCorrect!")
			correct_ans_count += 1
		else:
			print("\nWrong")
			print("\nCorrect choice is - ")
			print("{}. {}".format(correct_choice, defn))
		print("Example - {}".format(example))

	print("\nYou got {0} correct out of {1}. Accuracy = {2:.2f}%".format(correct_ans_count, game_count, correct_ans_count/game_count * 100))
	if correct_ans_count != game_count:
		print("Play more to improve your score!\n")
	else:
		print("You got all correct! Please contact the developer at mailsforyashj@gmail.com and let him know how you have improved your English vocabulary.\n")

if __name__ == '__main__':
	main()