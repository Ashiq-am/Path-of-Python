import pandas as pd

# Creating a Pandas Series
pd_series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("Pandas Series:")
print(pd_series)

# Accessing elements by index
element_b = pd_series['b']
print("Element at index 'b':", element_b)
