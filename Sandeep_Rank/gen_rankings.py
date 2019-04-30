import _pickle
import argparse
import os
from copy import deepcopy

from trec_car.format_runs import *

from sandeep_ranking import SANDEEP
from sandeep_prec import SANDEEP_PREC
from sandeep_newbm25 import SANDEEP_BM
from read_files import readFiles


parser = argparse.ArgumentParser()
parser.add_argument("outline_file", type=str, help="Qualified location of the outline file")
parser.add_argument("paragraph_file", type=str, help="Qualified location of the paragraph file")
parser.add_argument("output_file", type=str, help="Name of the output file")
parser.add_argument("ranking_function", type=str, help="SANDEEP")
parser.add_argument("passages_extract", type=int, help="no of passages to extract")
args = vars(parser.parse_args())

query_cbor = args['outline_file']
paragraphs_cbor = args['paragraph_file']
output_file_name = args['output_file']
algorithm = args['ranking_function']
passages_extract = args['passages_extract']

query_structure = None
document_structure = None
logic_instance = None


if algorithm == 'SANDEEP':
    logic_instance = None
    read_files = readFiles(query_cbor, paragraphs_cbor, passages_extract)
    query_structure = read_files.get_queries()
    document_structure = read_files.get_paragraphs_from_cbor()
    print("No of queries" + str(len(query_structure)))
    print("No of documents" + str(len(document_structure)))
    logic_instance = SANDEEP(query_structure, document_structure)


elif algorithm == 'SANDEEP_BM':
    logic_instance = None
    read_files = readFiles(query_cbor, paragraphs_cbor, passages_extract)
    query_structure = read_files.get_queries()
    document_structure = read_files.get_paragraphs_from_cbor()
    print("No of queries" + str(len(query_structure)))
    print("No of documents" + str(len(document_structure)))
    logic_instance = SANDEEP_BM(query_structure, document_structure)


# Generate the query scores
print("Generating the output structure by calculating scores................\n")
query_scores = dict()
queries_parsed = 0
for query in query_structure:
    temp_list = []
    top_n_list = []
    # print(queries_parsed)
    for key, value in document_structure.items():
        temp_list.append(logic_instance.SANDEEP_Score(query, key))
    temp_list.sort(key=lambda m: m[2])
    temp_list.reverse()
    # sorted(temp_list, key = lambda x: x[1], reverse = True)
    for elem in temp_list:
        top_n_list.append((elem[0][1], elem[1], elem[2]))
    query_scores[query[1]] = deepcopy(top_n_list)
    queries_parsed += 1


# Write the results to a file
print("Writing output to file...............................................\n")
with open(output_file_name, mode='w', encoding='UTF-8') as f:
    writer = f
    temp_list = []
    count = 0
    for k3, value in query_scores.items():
        count += 1
        rank = 0
        for x in value:
            rank += 1
            temp_list.append(RankingEntry(x[0], x[1], rank, x[2]))
    format_run(writer, temp_list, exp_name='test')
    f.close()