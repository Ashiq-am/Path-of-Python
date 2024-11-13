# Python code to find count of unique list in list of list

# Importing counter from collection
from collections import Counter

# Input list initialization
lst = [[1, 2, 3], [4, 5, 6], [3, 2, 1], [1, 2, 3]]

# Using counter
Output = Counter([tuple(i) for i in lst])

# Printing output
print(Output)
