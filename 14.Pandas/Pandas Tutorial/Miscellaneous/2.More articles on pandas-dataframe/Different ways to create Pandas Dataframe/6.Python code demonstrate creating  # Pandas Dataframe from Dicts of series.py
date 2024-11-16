# Python code demonstrate creating
# Pandas Dataframe from Dicts of series.

import pandas as pd

# Intialise data to Dicts of series.
d = {'one' : pd.Series([10, 20, 30, 40], index =['a', 'b', 'c', 'd']),
	'two' : pd.Series([10, 20, 30, 40], index =['a', 'b', 'c', 'd'])}

# creates Dataframe.
df = pd.DataFrame(d)

# print the data.
df
