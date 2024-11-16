# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating dictionary
dic = {'A': [1, 2, 3, 4, 0, np.nan, 3],
	'B': [3, 1, 4, 5, 0, np.nan, 5],
	'C': [0, 0, 0, 0, 0, 0, 0]}

# making dataframe using dictionary
data = pd.DataFrame(dic)

# calling data.any column wise
result = data.any(axis = 0)

# displaying result
result
