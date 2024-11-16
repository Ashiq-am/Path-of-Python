# import pandas library as pd
import pandas as pd

# create an Empty DataFrame object With
# column names and indices
df = pd.DataFrame(columns = ['Name', 'Articles', 'Improved'],
				index = ['a', 'b', 'c'])

print("Empty DataFrame With NaN values : \n\n", df)

# adding rows to an empty
# dataframe at existing index
df.loc['a'] = ['Ankita', 50, 100]
df.loc['b'] = ['Ankit', 60, 120]
df.loc['c'] = ['Harsh', 30, 60]

df
