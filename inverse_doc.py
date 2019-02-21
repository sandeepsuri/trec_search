import doc_prep
from doc_prep import *

#Ranking functions
import math
from textblob import TextBlob as tb 

def tf(word, doc):
	return doc.count(word) / len(doc)

def n_containing(word, doclist):
	return sum(1 for doc in doclist if word in doc)

def idf(word, doclist):
	return math.log(len(doclist) / (0.01 + n_containing(word, doclist)))

def tfidf(word, doc, doclist):
	return(tf(word, doc) * idf(word, doclist))



import re
import numpy as np



"""
Creating an inverse Index which gives 
the document number for each document and 
where words appear
"""

l = plot_data_nltk[0]
flatten = [item for sublist in l for item in sublist]
words = flatten
wordsunique = set(words)
wordsunique = list(wordsunique)


"""
Creating dictionary of words
THIS ONE-TIME INDEXING IS THE MOST PROCESSOR-
INTENSIVE STEP AND WILL TAKE 
TIME TO RUN 
(BUT ONLY NEEDS TO BE RUN ONCE)
"""
plottest = plot_data_nltk[0][0:1000]
worddic = {}

for doc in plottest:
	for word in wordsunique:
		if word in doc:
			word = str(word)
			index = plottest.index(doc)
			positions = list(np.where(np.array(plottest[index]) == word)[0])
			idfs = tfidf(word,doc,plottest)

			try:
				worddic[word].append([index, positions, idfs])
			except:
				worddic[word] = []
				worddic[word].append([index, positions, idfs])


print(worddic['china'])




























