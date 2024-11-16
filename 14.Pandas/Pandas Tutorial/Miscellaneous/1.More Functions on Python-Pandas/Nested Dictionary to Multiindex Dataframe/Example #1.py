# Import module
import pandas as pd

# Nested dictionary to convert it
# into multiindex dataframe
nested_dict = {'A': {'a': [1, 2, 3,
						4, 5],
					'b': [6, 7, 8,
						9, 10]},

			'B': {'a': [11, 12, 13,
						14, 15],
					'b': [16, 17, 18,
						19, 20]}}

reformed_dict = {}
for outerKey, innerDict in nested_dict.items():
	for innerKey, values in innerDict.items():
		reformed_dict[(outerKey,
					innerKey)] = values

# Multiindex dataframe
reformed_dict
