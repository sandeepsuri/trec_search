import argparse

from collections import Counter
Counter(word_list).most_common()

# parser = argparse.ArgumentParser()
# parser.add_argument("outline_file", type=str, help="Qualified location of the outline file")
# parser.add_argument("paragraph_file", type=str, help="Qualified location of the paragraph file")
# parser.add_argument("output_file", type=str, help="Name of the output file")
# parser.add_argument("ranking_function", type=str, help="SANDEEP")
# parser.add_argument("passages_extract", type=int, help="no of passages to extract")
# args = vars(parser.parse_args())

# query_cbor = args['outline_file']
# paragraphs_cbor = args['paragraph_file']
# output_file_name = args['output_file']
# algorithm = args['ranking_function']
# passages_extract = args['passages_extract']

# My Code
parser = argparse.ArgumentParser()

parser.add_argument("cbor_outline", type=str)
parser.add_argument("cbor_para", type=str)

args = vars(parser.parse_args())
if (args.cbor_outline) & (args.cbor_para):
	print("outline output and paragraph argument good")



# Initializing Dictionary
query_scores = {}

# counting number of times each word comes up in list of words (in dictionary)
for word in word_list: 
    query_scores[word] = query_scores.get(word, 0) + 1


#Reverser the key and values so they can be sorted using tuples
word_freq = []
for key, value in d.items():
    word_freq.append((value, key))

"""
ANOTHER METHOD
"""
# Initializing Dictionary
query_scores = {}

# Count number of times each word comes up in list of words (in dictionary)
for word in word_list:
    if word not in d:
        query_scores[word] = 0
    query_scores[word] += 1



"""
ANOTHER METHOD
"""
# initializing a dictionary
query_scores = {};

# counting number of times each word comes up in list of words
for key in word_list: 
    query_scores[key] = query_scores.get(key, 0) + 1

sorted(query_scores.items(), key = lambda x: x[1], reverse = True)

@staticmethod
def query_formatting(input_text: str):
	snow_stem = SnowballStemmer("english")
	wordnet_lemmatizer = WordNetLemmatizer()
	# Treat every word the same, therefore lower it first
	# and remove any special characters 
	lower_text = input_text.lower()
	lower_text = re.sub('[^a-zA-Z0-9 \n]', '', lower_text)
	# Remove any stop words afterwards and stem words
	filtered_sentence = [word for word in lower_text.split() if not word in readFiles.stop_words]
	filtered_sentence = [wordnet_lemmatizer.lemmatize(word) for word in filtered_sentence]

	ranked_dict = dict()

	my_ranked_dict = {}

	for key in filtered_sentence:
		my_ranked_dict[key] = my_ranked_dict.get(key, 0) + 1
		print(key)

	sorted(my_ranked_dict.items(), key = lambda x: x[1], reverse = True)

	return my_ranked_dict

	for word in filtered_sentence:
		if word in ranked_dict:
			ranked_dict[word] += 1
			largest = -1
			theword = None
			for key, value in ranked_dict.items():
				print(key, value)
				if value > largest:
					largest = value
					theword = word
					print('The Words: ', theword, largest)
					# print(word)
		else: 
			ranked_dict[word] = 1
			# print('**NEW**\n' + word)
	return ranked_dict




# Generate the query scores
print("Generating the output structure by calculating scores................\n")
query_scores = dict()
queries_parsed = 0
for query in query_structure:
    temp_list = []
    top_n_list = []
    # print(queries_parsed)
    for key, value in document_structure.items():
    	query_scores[key] = temp_list.get(key, 0) + 1
        temp_list.append(logic_instance.SANDEEP_Score(query, key))
    sorted(temp_list.items(), key = lambda x: x[1], reverse = True)
    temp_list.sort(key = lambda x: x[2], reverse = True)
    for elem in temp_list:
        # top_n_list.append((elem[0][1], elem[1], elem[2]))
        top_n_list.append((elem[0][1], elem[1], elem[2]))
    query_scores[query[1]] = deepcopy(top_n_list)
    queries_parsed += 1










