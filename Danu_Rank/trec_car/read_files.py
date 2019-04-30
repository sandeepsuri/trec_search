import read_data
import format_runs
import mmap
import re
import nltk
import sys
import math
import random
import collections
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


intro_msg = "Hello, welcome to the trec program"

from collections import defaultdict
intro_msg2 = "Here is the list of the following query files:\n "
choice = "Choose between: \n 1. pages \n 2. paragraphs"

print(intro_msg)
print(intro_msg2 + choice)


pages = ["train.pages.cbor", "train.test200.cbor", "train.pages.cbor-article.entity.qrels"]

paragraphs = ["train.test200.fold0.cbor.paragraphs", "train.test200.cbor", "train.pages.cbor"]

print("Select a number: ")

while True:
	x = int(input("> "))

	if x == 1:
		print(pages)
		print("\nWhich data would you like to see?\n")
		
		while True:
			y = int(input("> "))
			if y == 1:
				for page in read_data.iter_annotations(open(pages[0], 'rb')):
					print(page.page_id)
				break

			if y == 2:
				for page in read_data.iter_annotations(open(pages[1], 'rb')):
					print(page.page_id)
				break

			if y == 3:
				for page in read_data.iter_annotations(open(pages[2], 'rb')):
					print(page.page_id)
				break

			else:
				print("That's an invalid choice, try again.")
		break

	if x == 2:
		print(paragraphs)
		print("\nWhich data would you like to see?\n")

		while True:
			y = int(input("> "))
			if y == 1:
				for para in read_data.iter_pages(open(paragraphs[0], 'rb')):
					contents = para.get_text()
					file = open("textfile_1.txt", "w")
					file.write(contents)
					file.close()
				break

			if y == 2:
				for para in read_data.iter_pages(open('train.test200.cbor', 'rb')):
					contents = para.get_text()
					file = open("textfile_2.txt", "w")
					file.write(contents)
					file.close()
				break

			if y == 3:
				for para in read_data.iter_pages(open(paragraphs[2], 'rb')):
					contents = para.get_text()
					file = open("textfile_3.txt", "w")
					file.write(contents)

					def txt2paragraph(filepath):
					    with open(contents) as f:
					        lines = f.readlines()

					    paragraph = ''
					    for line in lines:
					        if line.isspace():  # is it an empty line?
					            if paragraph:
					                yield paragraph
					                paragraph = ''
					            else:
					                continue
					        else:
					            paragraph += ' ' + line.strip()
					    yield paragraph

					file.close()
				break

			else:
				print("That's an invalid choice, try again.")
		break

	else:
		print("That's an invalid choice, try again. ")


# class Task(object):	
# 	out = int((input("Would you like to rank the: \n1. Words \n2. Bigrams \n")))
# 	if out == 1:
# 		def rank(self):
# 			return Ranked()

# 	elif out == 2:
# 		def pair(self):
# 			return Paired()

# class Ranked(object):
# 	word_count = {}
# 	text = str(input('Enter the filename: '))

# 	with open(text, 'r') as inFile:
# 		for word in inFile:

# 			if word not in word_count:
# 				word_count[word.strip()] = 1
# 			else:
# 				word_count[word] = word_count[word] + 1

# 	# printing the words and its occurrence
# 	for (word, count) in word_count.items():
# 		print('{:15}{:3}'.format(word, count))




# class Paired(object):
# 	text = contents.split()
# 	counts = defaultdict(int)

# 	for pair in nltk.bigrams(text):
# 		counts[pair] += 1

# 		for c, pain in ((c, pair) for pair, c in counts.items()):
# 			print(pair, c)


#Word Count
class wordCount(object):
	lines = 0
	nwords = 0
	fname = str(input('Enter filename: '))

	#Total Wordcount 
	with open(fname, 'r') as f:
		for line in f:
			words = line.split()
			lines += 1
			nwords += len(words)

	# #Frequent Words
	# word_c = re.findall(r'\w+', open(fname).read().lower())
	# most_common = collections.Counter(words).most_common()
	# print(most_common)

	word_c = open(fname).read()

	stopwords = set(line.strip() for line in open('stopwords.txt'))
	stopwords = stopwords.union(set(['mr','mrs','one','two','said']))
	wordcount = {}

	# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
	for word in word_c.lower().split():
	    word = word.replace(".","")
	    word = word.replace(",","")
	    word = word.replace(":","")
	    word = word.replace("\"","")
	    word = word.replace("!","")
	    word = word.replace("â€œ","")
	    word = word.replace("â€˜","")
	    word = word.replace("*","")

	    if word not in stopwords:
	    	if word not in wordcount:
	    		wordcount[word] = 1
    		else:
    			wordcount[word] += 1

	#Print most common word
	print('Total word count: ' + str(nwords))
	n_print = int(input("\n\nHow many most common words to print: "))
	print("\nOK. The {} most common words are as follows\n".format(n_print))
	word_counter = collections.Counter(wordcount)

	for word, count in word_counter.most_common(n_print):
		print(word, ": ", count)
	file.close()

	#Creating a datafram of common words
	#Bar Graph
	lst =  word_counter.most_common(n_print)
	df = pd.DataFrame(lst, columns = ['Word', 'Count'])
	df.plot.bar(x = 'Word', y = 'Count')
	plt.savefig(input("Save graph as a png: "))


	



	
