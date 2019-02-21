#Loading all Libraries
import pandas as pd
import numpy as np 
import string
import random
import nltk

#My own files
import os
import glob

os.path.exists('my_corpus')
all_files = os.listdir("my_corpus/")
#Picking one of the text files
fpath = os.path.join('my_corpus', "textfile_2.txt")
f = open(fpath)

from nltk.corpus import brown
from nltk.corpus import stopwords

#Corpus built in nltk
from nltk.corpus import reuters

from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer


"""
COLOURED TEXT TO DIFFERENTIATE OUTPUT
YOU CAN DELETE THIS AFTERWARDS IF YOU WANT
ITS JUST HERE TO COMPARE MY CODE(BLUE) WITH
THE REFERENCE CODE (RED)
"""
RED = '\033[91m'
BLUE = '\033[94m'
END = '\033[0m'


"""
	LOADING FILES FROM CORPUS
"""

#Loading files from nltk corpus
n_corp = len(reuters.fileids())
# print(RED + 'Nltk corpus length: ' + END + str(n_corp))

#Loading files from my corpus and printing total files
my_corp = len(all_files)
# print(BLUE + 'My corpus length: ' + END + str(my_corp))



"""
	VIEWING TEXT FROM CORPUS
"""

#Viewing text from nltk corpus
reuters.raw(fileids=['test/14826'])[0:201]
# print(RED + '\n\nNLTK content:\n' + END + reuters.raw(fileids=['test/14826'])[0:201])

#Viewing text from my corpus
my_cont = f.read()[0:201]
# print(BLUE + '\n\nMy content:\n' + END + my_cont + '\n\n')




"""
	REMOVING PUNCTUATION
"""

#Removing punctuation from all DOCs from nltk corpus
exclude = set(string.punctuation)
alldocslist_nltk = []

#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
#This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

for index, i in enumerate(reuters.fileids()):
	text = reuters.raw(fileids=[i])
	text = ''.join(ch for ch in text if ch not in exclude)
	alldocslist_nltk.append(text)

# print(RED + 'From NLTK:\n' + END + alldocslist_nltk[1] + '\n\n')


#Removing from my document
alldocslist_mine = []

for file in glob.glob('my_corpus/*.txt'):
	for line in open(file):
		text = ''.join(char for char in line if char not in exclude)
		alldocslist_mine.append(text)

# print(BLUE + 'Mine:\n' + END + alldocslist_mine[0])



"""
	TOKENIZING WORDS
"""

#Tokenizing word in the Document, NLTK
plot_data_nltk = [[]] * len(alldocslist_nltk)

for doc in alldocslist_nltk:
	text = doc
	token_text = word_tokenize(text)
	plot_data_nltk[index].append(token_text)

# print(RED + '\n\nNLTK tokenized words:\n' + END + str(plot_data_nltk[0][1][0:10]))


#Tokenizing word in the Documents, Mine
plot_data_mine = [[]]

for file in glob.glob('my_corpus/*.txt'):
	for line in open(file):
		text = word_tokenize(line)
		plot_data_mine.append(text)

# print(BLUE + '\n\nMy tokenized words:\n' + END + str(plot_data_mine[1][0:10]))


"""
	MAKING ALL WORDS LOWERCASE
"""

#Lowercase for NLTK
for x in range(len(reuters.fileids())):
	lowers = [word.lower() for word in plot_data_nltk[0][x]]
	plot_data_nltk[0][x] = lowers

# print(RED + '\n\nNLTK Lowercased: ' + END + str(plot_data_nltk[0][1][0:10]))

#Lowercase for My Corpus
for x in range(len(glob.glob('my_corpus/*.txt'))):
	lowers = [word.lower() for word in plot_data_mine[x]]
	plot_data_mine[x] = lowers

# print(BLUE + '\n\nMy Lowercased: ' + END + str(plot_data_mine[1][0:10]))



"""
	GETTING RID OF STOPWORDS
"""
#Stopwords for NLTK
stop_words = set(stopwords.words('english'))

for x in range(len(reuters.fileids())):
	filtered_sentence = [w for w in plot_data_nltk[0][x] if not w in stop_words]
	plot_data_nltk[0][x] = filtered_sentence

# print(RED + '\n\nNLTK Stopwords Added: ' + END + str(plot_data_nltk[0][1][0:10]))

#Stopwords for my corpus
stop_words = set(stopwords.words('english'))

for x in range(len(glob.glob('my_corpus/*.txt'))):
	filtered_sentence = [w for w in plot_data_mine[x] if not w in stop_words]
	plot_data_mine[x] = filtered_sentence

#print(BLUE + '\n\nNLTK Stopwords Added: ' + END + str(plot_data_nltk[1][0:10]))


"""
	STEM WORDS
"""
#Stem words for My Corpus
for x in range(len(glob.glob('my_corpus/*.txt'))):
	snowball_stemmer = SnowballStemmer("english")
	stemmmed_text = [snowball_stemmer.stem(w) for w in plot_data_mine[x]]
	plot_data_mine[x] = stemmmed_text

# print('\n\n' + str(plot_data_mine[1][0:10]))













































































