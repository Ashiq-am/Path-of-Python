# Python program to collapse
# multiple Columns using Pandas
import pandas as pd
df = pd.DataFrame({'First': ['Manan ', 'Raghav ', 'Sunny '],
				'Last': ['Goel', 'Sharma', 'Chawla'],
				'Age':[12, 24, 56]})

mapping = {'First': 'Full Name', 'Last': 'Full Name'}

df = df.set_index('Age').groupby(mapping, axis = 1).sum()

df.reset_index(level = 0)
