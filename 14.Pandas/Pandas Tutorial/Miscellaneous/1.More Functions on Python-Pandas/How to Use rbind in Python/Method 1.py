# import pandas module
import pandas as pd

# create first dataframe
data1 = pd.DataFrame({'fruits': ['apple', 'guava', 'mango', 'banana'],
					'cost': [34, 56, 65, 45]})

# create second dataframe
data2 = pd.DataFrame({'fruits': ['cuatard apple', 'guava', 'mango', 'papaya'],
					'cost': [314, 86, 65, 51]})

# concat two columns
pd.concat([data1, data2])
