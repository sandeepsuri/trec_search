import math
from read_files import readFiles




class SANDEEP:

	docs_dict = dict()
	avg_doc_length = 0.0
	


	#Constructor
	def __init__(self, structure_of_query, structure_of_doc):
		self.query = structure_of_query
		self.documents = structure_of_doc
		self.total_docs = len(self.documents)
		# self.average_of_all_docs = self.document_length_avg()
		self.average_of_all_docs = self.new_document_length_avg()
		self.cache = dict()
		# Parameters for variables
		self.b = 0
		self.k = 0



	def document_length_avg(self):
		summ = 0
		for para_id, ranked_words_dict in self.documents.items():
			summ += sum(ranked_words_dict.values())
		return summ / float(self.total_docs)

	def new_document_length_avg(self):
		summ = 0
		for bodies, ranked_words_dict in self.documents.items():
			summ += sum(ranked_words_dict.values())
		return summ / float(self.total_docs)

	def document_word_freq(self, query_word):
		if query_word in SANDEEP.docs_dict:
			return float(SANDEEP.docs_dict[query_word])
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

	# def get_norm(self, query, document_id):
	# 	for key, value in query[2].items():
	# 		tf = self.freq_of_word(key, document_id)
	# 		norm = 1 - self.b + self.b*(mag_document/(self.average_of_all_docs + 1))



	
	def SANDEEP_Score(self, query, document_id):
		score = 0
		tf_idf = 0
		t_docs = sum(self.documents[document_id].values())
		t_ques = sum(query[2].values())
		for key, value in query[2].items():
			# Relevant documents
			tf = self.freq_of_word(key, document_id)
			idf = self.idf(key)

			# The += is the summation of tf_idf
			tf_idf += tf * idf


		# # query_struct = readFiles.get_queries(document_id)
		# # qs = len(query_struct)

		for key, value in query[2].items():
			ranked_words_dict = self.documents[document_id]
			mag_document = sum(ranked_words_dict.values())
			norm = 1 - self.b + self.b*(mag_document/(self.average_of_all_docs + 1))

			# PLN: Gives 0.2935 and 0.2875 scores
			# score += tf_idf * ((1 + math.log(1 + tf))/norm) * idf

			# BM25: 0.3075 and 0.2997
			score += tf_idf * ( ((self.k + 1) * tf) / (tf + self.k*norm + 1) )

		tup = (query, document_id, score)
		return tup





















