# Python code to count unique sublist within list

# Importing
from collections import Counter
import pandas as pd

# Input list initialization
lst = [[1, 2, 3], [4, 5, 6], [3, 2, 1], [1, 2, 3]]

# Getting count
dict = Counter([tuple(i) for i in lst])

# Creating pandas dataframe
Output = pd.DataFrame(data ={'list': list(dict.keys()),
						'count': list(dict.values())})

# Printing output
print(Output)
