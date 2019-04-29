import math
from read_files import readFiles
import numpy as np
np.seterr(divide='ignore', invalid='ignore')



class SANDEEP_PREC:

	docs_dict = dict()
	avg_doc_length = 0.0
	


	#Constructor
	def __init__(self, structure_of_query, structure_of_doc):
		self.query = structure_of_query
		self.documents = structure_of_doc
		self.total_docs = len(self.documents)
		self.total_ques = len(self.query)
		self.average_of_all_docs = self.document_length_avg()
		self.cache = dict()
		# Parameters for variables
		self.b = 0
		self.k = 0



	def document_length_avg(self):
		summ = 0
		for para_id, ranked_words_dict in self.documents.items():
			summ += sum(ranked_words_dict.values())
		return summ / float(self.total_docs)

	def document_word_freq(self, query_word):
		if query_word in SANDEEP_PREC.docs_dict:
			return float(SANDEEP_PREC.docs_dict[query_word])
		else:
			if query_word in self.cache:
				return float(self.cache[query_word])
			else:
				word_in_doc = 0
				for para_id, ranked_words_dict in self.documents.items():
					if query_word in ranked_words_dict:
						word_in_doc += 1
				self.cache[query_word] = word_in_doc
				return float(word_in_doc)


	#Ranks word and puts them through normalizer 
	def freq_of_word(self, word, document_id):
		ranked_words_dict = self.documents[document_id]
		if word in ranked_words_dict:
			ranked_normalized = ranked_words_dict[word] 
			return ranked_normalized
		else:
			return 0


	"""
	IDF(W) = log[ (M+1) / (Total # of Docs containing word) ]
	"""
	def idf(self, query_word):
		t_docs = self.total_docs
		idf_score = t_docs * (1 + math.log((self.total_docs + 1) / (self.document_word_freq(query_word) + 0.5)))
		return idf_score


	
	def SANDEEP_Score(self, query, document_id):
		score = 0
		tf_idf = 0
		t_docs = sum(self.documents[document_id].values())
		t_ques = sum(query[2].values())
		for key, value in query[2].items():
			# Relevant documents
			tf = self.freq_of_word(key, document_id)
			idf = self.idf(key)
			tf_idf += tf * idf
			

		for key, value in query[2].items():
			ranked_words_dict = self.documents[document_id]
			mag_document = sum(ranked_words_dict.values())
			norm = 1 - self.b + self.b*(mag_document/(self.average_of_all_docs + 1))

			precision = (np.intersect1d(tf_idf, t_docs)) / t_docs
			recall = (np.intersect1d(tf_idf, t_docs))  / (tf)

			score += ((self.b)*precision*recall)/(self.b*precision + recall)

		tup = (query, document_id, score)
		return tup





















