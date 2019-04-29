import tagme
import os
import re


from trec_car.read_data import *

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

TAGME_TOKEN = "aab8856f-2362-4a64-a60d-5a6daddc51b1-843339462"
DEFAULT_LANG = "en"
DEFAULT_TAG_API = "https://tagme.d4science.org/tagme/tag"
DEFAULT_SPOT_API = "https://tagme.d4science.org/tagme/spot"
DEFAULT_REL_API = "https://tagme.d4science.org/tagme/rel"


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
				id_to_text[p.para_id] = readFiles.query_zipfs_law(p.get_text())
		return id_to_text


	def get_queries(self):
		query_tup_list = []
		for page in self.pages:
			for section_path in page.flat_headings_list():
				query_id_plain = " ".join([page.page_name] + [section.heading for section in section_path])
				query_id_formatted = "/".join([page.page_id] + [section.headingId for section in section_path])
				tup = (query_id_plain, query_id_formatted, readFiles.text_query_annotations(query_id_plain))
				query_tup_list.append(tup)
		return query_tup_list

	#processing text query with annotations
	@staticmethod
	def text_query_annotations(input_text: str):
		#  A reasonable threshold is between 0.1 and 0.3.
		annotations = tagme.annotate(input_text, TAGME_TOKEN)
		entities = " ".join([word.entity_title for word in annotations.get_annotations(0.18)])

		lunch_annotations = tagme.annotate("My favourite meal is Mexican burritos.")

		snow_stem = SnowballStemmer("english")
		# Treat every word the same, therefore lower it first
		# and remove any special characters 
		lower_text = (input_text + " " + entities).lower()
		lower_text = re.sub('[^a-zA-Z0-9 \n]', '', lower_text)
		# Remove any stop words afterwards and stem words
		filtered_sentence = [word for word in lower_text.split() if not word in readFiles.stop_words]
		filtered_sentence = [snow_stem.stem(word) for word in filtered_sentence]

		ranked_dict = dict()
		for word in filtered_sentence:
			if word in ranked_dict:
				ranked_dict[word] += 1
			else: 
				ranked_dict[word] = 1
		return ranked_dict


	#processing text query with stops
	@staticmethod
	def text_query_spots(input_text: str):
		mentions = tagme.mentions(input_text, TAGME_TOKEN)
		entities = " ".join([word.mention for word in mentions.get_mentions(0.01)])

		snow_stem = SnowballStemmer("english")
		# Treat every word the same, therefore lower it first
		# and remove any special characters 
		lower_text = (input_text + " " + entities).lower()
		lower_text = re.sub('[^a-zA-Z0-9 \n]', '', lower_text)
		# Remove any stop words afterwards and stem words
		filtered_sentence = [word for word in lower_text.split() if not w in readFiles.stop_words]
		filtered_sentence = [snow_stem.stem(word) for word in filtered_sentence]

		ranked_dict = dict()
		for word in filtered_sentence:
			if word in ranked_dict:
				ranked_dict[word] += 1
			else: 
				ranked_dict[word] = 1
		return ranked_dict