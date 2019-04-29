 
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
import cbor
import itertools
import typing

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


from collections import defaultdict

intro_msg = "Hello, welcome to the trec program"
intro_msg2 = "Here is the list of the following query files:\n "
choice = "Choose between: \n 1. pages \n 2. paragraphs"

print(intro_msg)
print(intro_msg2 + choice)


pages = ["train.pages.cbor", "train.test200.cbor", "train.test200.fold0.cbor"]

paragraphs = ["train.test200.fold0.cbor", "train.test200.cbor", "train.pages.cbor"]




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
				for para in read_data.iter_paragraphs(open(paragraphs[0], 'rb')):
					contents = para.get_text()
					paragraphid = para.para_id
					
					file = open('txt_3.txt', 'w')
					file.write(contents)
					file.close()

					file = open('txt_3_id.txt', 'w')
					file.write(paragraphid)
					file.close()
				break

			if y == 2:
				for para in read_data.iter_pages(open(paragraphs[1], 'rb')):
					contents = para.get_text()
					file = open("textfile_2.txt", "w")
					file.write(contents)
					file.close()
				break

			if y == 3:
				for para in read_data.iter_pages(open(paragraphs[2], 'rb')):
					contents = para.get_text()
					file = open("textfile_3.txt","w")	
					file.write(contents)
					file.close()
				break

			else:
				print("That's an invalid choice, try again.")
		break

	else:
		print("That's an invalid choice, try again. ")



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

# class Paragraphs:
#     def __init__(self, fileobj, separator='.'):
#         # self.seq: the underlying line-sequence
#         # self.line_num: current index into self.seq (line number)
#         # self.para_num: current index into self (paragraph number)
#         try: self.seq = fileobj
#         except AttributeError: self.seq = fileobj
#         self.line_num = 0
#         self.para_num = 0
#         # allow for optional passing of separator-function
#         if separator is '.':
#             def separator(line): return line == '\n'
#         elif not callable(separator):
#             raise TypeError("separator argument must be callable")
#         self.separator = separator
   
#     def __getitem__(self, index):
#         if index != self.para_num:
#             raise TypeError("Only sequential access supported")
#         self.para_num += 1
#         # start where we left off, and skip 0+ separator lines
#         i = self.line_num
#         while 1:
#             # note: if this raises IndexError, it's OK to propagate
#             # it, since we're also a finished-sequence in this case
#             line = self.seq[i]
#             i += 1
#             if not self.separator(line): break
#         # accumulate 1+ non-blank lines into list result
#         result = [line]
#         while 1:
#             # here we must intercept IndexError, since we're not
#             # finished, even when the underlying sequence is --
#             # we have one or more lines in result to be returned
#             try: line = self.seq[i]
#             except IndexError: break
#             i += 1
#             if self.separator(line): break
#             result.append(line)
#         # update self state, return string result
#         self.line_num = i
#         return ''.join(result)


# def show_paragraphs(filename, numpars = 5):
# 	pp = Paragraphs(open(filename).readlines())
# 	for p in pp:
# 		print("Par#%d, line# %d: %s" % (pp.para_num, pp.line_num, repr(p)))
# 		if pp.para_num > numpars: break


show_paragraphs('textfile_3.txt')











