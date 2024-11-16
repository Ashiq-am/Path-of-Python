# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series([19.5, 16.8, 22.78, 20.124, 18.1002])

# Create the Index
index_ = [5, 3, 2, 1, 4]

# set the index
sr.index = index_

# Print the series
print(sr)
