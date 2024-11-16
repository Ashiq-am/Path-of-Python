# importing pandas

import pandas as pd

# Creating dataframe a
a = pd.DataFrame()

# Creating Dictionary
d = {'id': [1, 2, 10, 12],
	'val1': ['a', 'b', 'c', 'd']}

a = pd.DataFrame(d)

# printing the dataframe
a
