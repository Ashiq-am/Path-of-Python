df = pd.read_csv("train/train.csv", chunksize=10)

for data in df:
	pprint(data)
	break
