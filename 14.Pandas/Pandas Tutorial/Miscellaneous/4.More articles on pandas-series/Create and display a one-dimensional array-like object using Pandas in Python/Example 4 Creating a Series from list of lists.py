# importing the module
import pandas as pd

# creating the data
data = [['g', 'e', 'e', 'k', 's'],
		['f', 'o', 'r'],
		['g', 'e', 'e', 'k', 's']]

# creating a Pandas series of lists
s = pd.Series(data)

# displaying the Series
print(s)
