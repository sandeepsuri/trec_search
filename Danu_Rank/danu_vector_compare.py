import math


class DANU_VectorCompare:

    def __init__(self, query_structure, document_structure):
        
        self.queries = query_structure
        self.documents = document_structure
        self.no_of_documents = len(self.documents)
        #self.average_length_of_all_documents = self.average_document_length()
        self.k = 1.2


    # concordance is the word count in a document
    '''
    def concordance(self):
        for key, value in self.documents.items():
        	document = value[1]

	        if type(document) != str:	    
	            raise ValueError('Supplied Argument should be of type string')
	        con = {}
	        for word in document.split(' '):
	            if word in con:
	            #if con.has_key(word):
	                con[word] = con[word] + 1
	            else:
	      	        con[word] = 1
	        return con	
    '''
    
    def magnitude(self, concordance):
        #concordance = concordance(self)
        if type(concordance) != dict:
            raise ValueError('Supplied Argument should be of type dict')
        total = 0
        for word,count in concordance.items():
            total += count ** 2
        return math.sqrt(total)	


    def relation(self,concordance1, concordance2):
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
        if (self.magnitude(concordance1) * self.magnitude(concordance2)) != 0:
            return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))
        else:
            return 0

   











