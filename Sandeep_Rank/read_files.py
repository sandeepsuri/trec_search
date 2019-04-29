import os
import re
import csv
import matplotlib.pyplot as plt
from scipy import special
import numpy as np
from operator import itemgetter


from trec_car.read_data import *

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer


class readFiles:
	stop_words = stopwords.words('english')
	# Create a dictionary of words
	cache_words = dict()

	# Constructor Class
	def __init__(self, outline_file, para_file, passage_to_extract):
		self.outline_file = outline_file
		self.para_file = para_file
		self.passages_extract = passage_to_extract
		self.pages = self.get_pages_from_cbor()

	# Get pages from the cbor files
	def get_pages_from_cbor(self):
		with open(self.outline_file, 'rb') as f:
			pages = [p for p in itertools.islice(iter_annotations(f), 0, 1000)]
		return pages

	# Get paragraphs from cbor files
	def get_paragraphs_from_cbor(self):
		id_to_text = dict()
		with open(self.para_file, 'rb') as f:
			for p in itertools.islice(iter_paragraphs(f), 0, self.passages_extract):
				id_to_text[p.para_id] = readFiles.query_formatting(p.get_text())
		return id_to_text


	def get_queries(self):
		query_tup_list = []
		for page in self.pages:
			for section_path in page.flat_headings_list():
				query_id_plain = " ".join([page.page_name] + [section.heading for section in section_path])
				query_id_formatted = "/".join([page.page_id] + [section.headingId for section in section_path])
				tup = (query_id_plain, query_id_formatted, readFiles.query_formatting(query_id_plain), page.page_name)
				query_tup_list.append(tup)
		return query_tup_list


	@staticmethod
	def query_formatting(input_text: str):
		snow_stem = SnowballStemmer("english")
		# wordnet_lemmatizer = WordNetLemmatizer()
		# Treat every word the same, therefore lower it first
		# and remove any special characters 
		lower_text = input_text.lower()
		lower_text = re.sub('[^a-zA-Z0-9 \n]', '', lower_text)
		# Remove any stop words afterwards and stem words
		filtered_sentence = [word for word in lower_text.split() if not word in readFiles.stop_words]
		# filtered_sentence = [wordnet_lemmatizer.lemmatize(word) for word in filtered_sentence]
		filtered_sentence = [snow_stem.stem(word) for word in filtered_sentence]

		ranked_dict = dict()

		# for word in filtered_sentence:
		# 	ranked_dict[word] += ranked_dict.get(word, 0) + 1
		# 	print(ranked_dict)

		# sorted(ranked_dict.items(), key = lambda x: x[1], reverse = True)

		# return ranked_dict

		for word in filtered_sentence:
			if word in ranked_dict:
				ranked_dict[word] += 1
				largest = -1
				theword = None
				for key, value in ranked_dict.items():
					print(ranked_dict)
					if value > largest:
						largest = value
						theword = word
						print('The Words: ', theword, largest)
						# print(word)
			else: 
				ranked_dict[word] = 1
				# print('**NEW**\n' + word)

		return ranked_dict

		# a = 2
		# s = ranked_dict.values()
		# s = np.array(s)

		# x = np.arange(1., 50.)
		# y = x**(-a) / special.zetac(a)
		# plt.plot(x, y/max(y), linewidth=2, color = 'r')
		# plt.savefig('zipfs.png')

		




























