import pandas as pd

# Initializing a Series from a list
data = [1, 2, 3, 4, 5]
series_from_list = pd.Series(data)
print(series_from_list)

# Initializing a Series from a dictionary
data = {'a': 1, 'b': 2, 'c': 3}
series_from_dict = pd.Series(data)
print(series_from_dict)

# Initializing a Series with custom index
data = [1, 2, 3, 4, 5]
index = ['a', 'b', 'c', 'd', 'e']
series_custom_index = pd.Series(data, index=index)
print(series_custom_index)
