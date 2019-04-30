import math
from danu_vector_compare import DANU_VectorCompare


class DANU_WEIGHT_1:
    
    average_doc_length = 0.0
    no_of_docs_dict = dict()
    word_weight_relation = []

    def __init__(self, query_structure, document_structure):
        
        self.queries = query_structure
        self.documents = document_structure
        self.no_of_documents = len(self.documents)
        self.average_length_of_all_documents = self.average_document_length()
        self.k = 1.2
        self.n = 5.0


    def average_document_length(self):
        """
        Calculates the average length of documents 
        """
        summ = 0
        for para_id, ranked_words_dict in self.documents.items():
            summ += sum(ranked_words_dict.values())
        return summ / float(self.no_of_documents)


    def word_frequency_of_word_in_document(self, word, document_id):
        """
        Finds the frequency of a word in the document
        """
        if document_id in self.documents:
            ranked_words_dict = self.documents[document_id]
            if word in ranked_words_dict:
                return ranked_words_dict[word]
            else:
                return 0
        else:        
            return 0


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

    def vector_magnitude(self, concordance):
        #concordance = concordance(self)
        if type(concordance) != dict:
            raise ValueError('Supplied Argument should be of type dict')
        total = 0
        for word,count in concordance.items():
            total += count ** 2
        return math.sqrt(total) 


    def vector_relation(self,concordance1, concordance2):
        if type(concordance1) != dict:
            raise ValueError('Supplied Argument 1 should be of type dict')
        if type(concordance2) != dict:
            raise ValueError('Supplied Argument 2 should be of type dict')
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
            #if concordance2.has_key(word):
                topvalue += count * concordance2[word]
        if (self.vector_magnitude(concordance1) * self.vector_magnitude(concordance2)) != 0:
            return topvalue / (self.vector_magnitude(concordance1) * self.vector_magnitude(concordance2))
        else:
            return 0    


    def similarity_top_document(self):
        sum_sim = 0
        doc_val = []

        for key, value in self.documents.items():
            doc_val.append(value)

        for value1 in doc_val:
            for value2 in doc_val:
                if value1 != value2:
                    rel = self.vector_relation(value1, value2)
                    #print (rel)
                    sum_sim += rel

        return sum_sim/2    # /2 used to eliminate duplicate pairs of relation values


    def weight(self, query_word, document_id):

        rel_of_doc = self.similarity_top_document()/(self.no_of_documents - 1)
        query_idf = self.modified_idf_calculation(query_word)
        term_freq = self.word_frequency_of_word_in_document(query_word, document_id)

        weight = math.log(1 + term_freq * query_idf * rel_of_doc)

        tup = (query_word, weight)
        return tup


    def score_max(self, query, query_word_relation, document_id):

        max_weight = 0

        for q_key, q_value in query[2].items():
            weight = self.weight(q_key, document_id)

            if q_key in query_word_relation:
                q_value1 = query_word_relation.get(q_key)
                
                weight1 = weight[1]

                if (weight1 < q_value1):
                    weight1 = q_value1

            if (max_weight < weight1):
                max_weight = weight1
        
        score = max_weight

        tup = (query, document_id, score)
        return tup           




        

















