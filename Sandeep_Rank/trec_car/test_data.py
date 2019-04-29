import read_data

for list in read_data.List(open('train.test200.cbor', 'rb')):
	print(list.get_text())
