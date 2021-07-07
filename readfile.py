import os

from sys import argv
from string import punctuation
from collections import *

#filename = "peterparktv.log"
basepath = os.getcwd()
my_path = os.path.join(basepath, 'chatlogs')

keyWords = ['KEKW', 'Kekw', 'LOL', 'LUL', 'lol', 'Lol', 'Pog', 'POG', 'OMG']

# with open(inputfile) as file_object:
#     for line in file_object:

# for one_filename in argv[1:]:

#     print("Text file to import and read:", one_filename)
#     print("\nReading file...\n")

#     text_file = open(one_filename, 'r')
#     all_lines = text_file.readlines()
#     text_file.close()

#     print("\nFile read finished!")

#     word_freq = Counter([word.strip(punctuation) for line in all_lines for word in line.split()])

#     print("Append result to the end of file: List_of_words.txt")

#     output_file = open("List_of_words.txt", "a")

#     for word in keyWords:
#         if word in word_freq:
#             output_file.write( "%s: %d\n" % (word, word_freq[word]) )

#     output_file.close()

def count_word(filename, word):
	""" Counts the number of times a certain word appears in the file. """
	with open(filename) as file:
		content = file.read()
		num_words = content.lower().count(word)
		return f"Number of times '{word}' appears in {entry.name}: {num_words}"

with os.scandir(my_path) as entries:
	for entry in entries:
		if entry.is_file() and not entry.name.startswith("."):
			print(count_word(entry, 'kekw'))
			print(count_word(entry, 'pog'))
			print(count_word(entry, 'poggers'))
			print(count_word(entry, 'lol'))
			print(count_word(entry, 'lul'))