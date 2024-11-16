# Python program to convert
# dictionary to numpy array

# Import required package
import numpy as np

# Creating a Nested Dictionary
dict = {1: 'Geeks',
		2: 'For',
		3: {'A': 'Welcome',
			'B': 'To',
			'C': 'Geeks'}
		}

# to return a group of the key-value
# pairs in the dictionary
result = dict.items()

# Convert object to a list
data = list(result)

# Convert list to an array
numpyArray = np.array(data)

# print the numpy array
print(numpyArray)
