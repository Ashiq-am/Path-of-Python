# import pandas library
import pandas as pd

# list of Tuples
data = [
		(20, 16, 23),
		(30, None, 11),
		(40, 34, 11),
		(50, 35, None),
		(60, 40, 13)
		]

# creating a DataFrame object
df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd', 'e'],
					columns = ['x', 'y', 'z'])

# get the index position\label of
# minimum values in every row
minvalueIndexLabel = df.idxmin(axis = 1)

minvalueIndexLabel
