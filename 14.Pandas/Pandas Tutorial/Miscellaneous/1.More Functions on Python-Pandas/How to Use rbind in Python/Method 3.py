# import pandas module
import pandas as pd

# create first dataframe with 2 columns
data1 = pd.DataFrame({'fruits': ['apple', 'guava', 'mango', 'banana'],
					'cost': [34, 56, 65, 45]})

# create second dataframe with 3 columns
data2 = pd.DataFrame({'fruits': ['cuatard apple', 'guava', 'mango', 'papaya'],
					'cost': [314, 86, 65, 51],
					'city': ['guntur', 'tenali', 'ponnur', 'hyd']})

# concat two columns
pd.concat([data1, data2]).reset_index(drop=True)
