# importing pandas as pd
import pandas as pd

# Creating an array
array = ['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio']

# Create the Index
index_ = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5']

# Creating the series
sr = pd.Series.from_array(arr = array, index = index_)

# Print the series
print(sr)
