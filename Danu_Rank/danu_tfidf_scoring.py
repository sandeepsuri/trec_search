import math
from danu_weight_score_1 import DANU_WEIGHT_1 

class TFIDF:

    no_of_docs_dict = dict()
    average_doc_length = 0.0
    

    def __init__(self, query_structure, document_structure):
        """
        Constructor
        :param query_structure: tuple tuple (query_id_plain, query_id_formatted, Ranked dict of words))
        :param document_structure: 
        """
        self.queries = query_structure
        self.documents = document_structure
        #self.weght_coeff = weight_treatment
        self.no_of_documents = len(self.documents)
        self.average_length_of_all_documents = self.average_document_length()
        self.k = 1.2
        self.b = 0.75
        self.delta = 1.0
        self.k_plus_one = self.k + 1

    def average_document_length(self):
        """
        Calculates the average length of documents 
        """
        summ = 0
        for para_id, ranked_words_dict in self.documents.items():
            summ += sum(ranked_words_dict.values())
        return summ / float(self.no_of_documents)

    def modified_idf_calculation(self, query_word):
        """
        Modified IDF calculation for T DELTA IDF
        """
        return math.log((self.no_of_documents + 1) / (self.no_of_documents_containing_a_word(query_word) + 0.5))

    def no_of_documents_containing_a_word(self, query_word):
        """
        Returns the no of documents containing a word
        """
        no_of_documents_having_the_word = 0
        for para_id, ranked_word_dict in self.documents.items():
            if query_word in ranked_word_dict:
                no_of_documents_having_the_word += 1
        return float(no_of_documents_having_the_word)

    def word_frequency_of_word_in_document(self, word, document_id):
        """
        Finds the frequency of a word in the document
        """
        ranked_words_dict = self.documents[document_id]
        if word in ranked_words_dict:
            return ranked_words_dict[word]
        else:
            return 0

    def score(self, query, document_id):
        """
        Given a query and a document calculates the score
        """
        score = 0
        document_length = sum(self.documents[document_id].values())
        for key, value in query[2].items():
            w = self.word_frequency_of_word_in_document(key, document_id)
            d = 1 - self.b + self.b * (document_length / self.average_length_of_all_documents)
            w_by_plus_delta_ln = 1.0 + math.log((w / d) + self.delta)
            outer_ln = 1.0 + math.log(w_by_plus_delta_ln)
            score += self.modified_idf_calculation(key) * outer_ln
        tup = (query, document_id, score)
        return tup


     
