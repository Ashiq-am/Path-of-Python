# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series([248])

# Create the Index
index_ = ['Coca Cola']

# set the index
sr.index = index_

# Print the series
print(sr)
