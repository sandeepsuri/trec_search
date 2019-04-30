import math 
import _pickle
import argparse
import os
from copy import deepcopy

#from danu_vector_compare import DANU_VectorCompare
from danu_weight_score_1 import DANU_WEIGHT_1
from danu_tfidf_scoring import TFIDF

from trec_car.format_runs import *

from danu_ranking import Ranking


word_weight_relation = {}

parser = argparse.ArgumentParser()
parser.add_argument("outline_file", type=str, help="Qualified location of the outline file")
parser.add_argument("paragraph_file", type=str, help="Qualified location of the paragraph file")
parser.add_argument("output_file_name", type=str, help="Name of the output run file")
parser.add_argument("ranking_function", type=str, help="RANK1")
parser.add_argument("passages_extract", type=int, help="no of passages to extract")
parser.add_argument("top_n_doc_count", type=int, help="no of documents to use for the weighing function")
args = vars(parser.parse_args())

query_cbor = args['outline_file']
paragraphs_cbor = args['paragraph_file']
output_file_name = args['output_file_name']
algorithm = args['ranking_function']
passages_extract = args['passages_extract']
top_n_doc_count = args['top_n_doc_count']

query_structure = None
document_structure = None
logic_instance = None


if algorithm == 'RANK1':
    logic_instance = None
    ranking = Ranking(query_cbor, paragraphs_cbor, passages_extract)
    query_structure = ranking.gather_queries()
    document_structure = ranking.gather_paragraphs()
    print("No of queries: " + str(len(query_structure)))
    print("No of documents: " + str(len(document_structure)))
    print("No of docs for weighing: " + str(top_n_doc_count))
    logic_instance = TFIDF(query_structure, document_structure)


# Generate the query scores for PHASE 1
print("Generating the output structure by calculating scores................\n")
query_scores = dict()
queries_parsed = 0
for query in query_structure:
    temp_list = []
    top_n_list = []
    #print(queries_parsed)
    for key, value in document_structure.items():
        temp_list.append(logic_instance.score(query, key))
    temp_list.sort(key=lambda m: m[2])
    temp_list.reverse()
    for elem in temp_list:
        top_n_list.append((elem[0][1], elem[1], elem[2]))
    query_scores[query[1]] = deepcopy(top_n_list)
    queries_parsed += 1

print ('creating top_doc_structure')

# Display only the top number of ranked documents
if (top_n_doc_count > passages_extract):
    top_n_doc_count = passages_extract

count = 0
top_doc_structure = {}

for tup in top_n_list:
    count += 1
    key = tup[1]
    value = document_structure.get(key)
    top_doc_structure[key] = value
    if count == top_n_doc_count:
        break

#print (top_doc_structure) 

weight_funct = DANU_WEIGHT_1(query_structure, top_doc_structure)
'''
for key, value in document_structure.items():
    weight = weight_funct.weight('year', key)
    #print (weight)   
'''

print ('Creating word to weight dictionary')

# creating the word, weight dictionary
for query in query_structure:
    for q_key, q_value in query[2].items():
        weight_sum = 0
        for d_key, d_value in top_doc_structure.items():

            weight = weight_funct.weight(q_key, d_key)
            weight_sum += weight[1]
        weight_avg = weight_sum/top_n_doc_count
        if q_key in word_weight_relation:
            weight_value = word_weight_relation.get(q_key)
            if (weight_value < weight_avg):
                weight_value = weight_avg
                word_weight_relation[q_key] = weight_avg
        else:    
            word_weight_relation[q_key] = weight_avg

        #print (q_key)
        #print (weight_avg)    

#print (word_weight_relation)


# Generate the query scores for PHASE 3
print("Generating the output structure by calculating scores................\n")
query_scores1 = dict()
queries_parsed = 0
for query in query_structure:
    temp_list = []
    top_n_list = []
    #print(queries_parsed)
    for key, value in document_structure.items():
        weight_score = weight_funct.score_max(query, word_weight_relation, key)
        #print (weight_score[1] + str(weight_score[2]))
        
        temp_list.append(weight_score)
        
    temp_list.sort(key=lambda m: m[2])
    temp_list.reverse()

    for elem in temp_list:
        top_n_list.append((elem[0][1], elem[1], elem[2]))
    query_scores1[query[1]] = deepcopy(top_n_list)
    queries_parsed += 1


'''
for query in query_structure:
    for d_key, d_value in top_doc_structure.items():
    #for d_key, d_value in document_structure.items():
        tup = weight_funct.score_max(query, d_key)
        print (tup[0][1] + str(tup[2]))
'''

# Write the results to a file

print("Writing output to file...............................................\n")
with open(output_file_name, mode='w', encoding='UTF-8') as f:
    writer = f
    temp_list = []
    count = 0
    for k3, value in query_scores1.items():
        count += 1
        rank = 0
        for x in value:
            rank += 1
            temp_list.append(RankingEntry(x[0], x[1], rank, x[2]))
    format_run(writer, temp_list, exp_name='test')
    f.close()



