# import pandas library
import pandas as pd

# dictionary
dict = {'X': ['A', 'B', 'A', 'B'],
		'Y': [1, 4, 3, 2]}

# create a dataframe
df = pd.DataFrame(dict)

# group by "X" column
groups = df.groupby('X')

# extract keys from groups
keys = groups.groups.keys()

for i in keys:
	print(groups.get_group(i))
	print('\n')
