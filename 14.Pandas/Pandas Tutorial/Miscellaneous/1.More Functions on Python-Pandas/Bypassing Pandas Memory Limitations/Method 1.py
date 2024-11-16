import pandas as pd

data = pd.read_csv('train dataset.csv', chunksize=100)

for x in data:
	print(x.shape[0])
