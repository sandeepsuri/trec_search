import os
import inverse_doc
from inverse_doc import *



from collections import Counter


def search(search_sentence):
	try: 
		#split sentence into individual words
		search_sentence = search_sentence.lower()

		try:
			words = search_sentence.split(' ')
		except:
			words = list(words)
		enddic = {}
		idfdic = {}
		closedic = {}

		#remvoe words if not in worddic
		realwords = []
		for word in words:
			if word in list(worddic.keys()):
				realwords.append(word)

		words = realwords
		numwords = len(words)

		#make metric of number of occurances of all words in each doc
		for word in words:
			for indpos in worddic[word]:
				index = indpos[0]
				amount = len(indpos[1])
				idfscore = indpos[2]
				enddic[index] = amount
				idfdic[index] = idfscore

				fullcount_order = sorted(enddic.items(), key = lambda x:x[1], reverse = True)
				fullidf_order = sorted(idfdic.items(), key = lambda x:x[1], reverse = True)


		#make metric of what % of words appear in each doc
		combo = []
		alloptions = {k : worddic.get(k, None) for k in (words)}
		
		for worddex in list(alloptions.values()):
			for indexpos in worddex:
				for indexz in indexpos:
					combo.append(indexz)

		comboindex = combo[::3]
		combocount = Counter(comboindex)

		for key in combocount:
			combocount[key] = combocount[key] / numwords

		combocount_order = sorted(combocount.items(), key = lambda x:x[1], reverse = True)

		#make metric for if words appear in same order as in search
		if len(words) > 1:
			x = []
			y = []
			for record in [worddic[z] for z in words]:
				for index in record:
					x.append(index[0])

			for i in x:
				if x.count(i) > 1:
					y.append(i)

			y = list(set(y))

			closedic = {}
			for wordbig in [worddic[x] for x in words]:
				for record[0] in y:
					index = record[0]
					positions = record[i]

					try:
						closedic[index].append(positions)
					except:
						closedic[index] = []
						closedic[index].append(positions)



			x = 0
			fdic = {}

			for index in y:
				csum = []
				for seqlist in closedic[index]:
					while x > 0:
						secondlist = seqlist
						x = 0
						sol = [1 for i in firstlist if i + 1 in secondlist]
						csum.append(sol)

						fsum = [item for sublist in csum for item in sublist]
						fsum = sum(fsum)

						fdic[index] = fsum
						fdic_order = sorted(fdic.items(), key = lambda x:x[1], reverse = True)

					while x == 0:
						firstlist = seqlist
						x = x + 1

		else:
			fdic_order = 0



		return(search_sentence, words, fullcount_order, combocount_order, fullidf_order, fdic_order)

	except:
		return(" ")


result1 = search('china daily says what')
result2 = search('indonesia crude palm oil')
result3 = search('price of nickel')
result4 = search('north yemen sugar')
result5 = search('nippon steel')
result6 = search('Gutenberg')
result7 = search('Lincoln')
result8 = search('Benedict')

df = pd.DataFrame([[result1,result2,result3,result4,result5,result6,result7,result8]])
df.columns = ['', '', 'search term', 'actual_words_searched', 'num_occur', 'percentage_of_terms', 'td-idf', 'word_order'] 



with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)




























































