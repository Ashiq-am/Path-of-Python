# importing pandas as pd
import pandas as pd

# Creating the first Series
sr1 = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio'])

# Create the Index
index_ = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5']

# set the index
sr1.index = index_

# Print the series
print(sr1)

# Creating the second Series
sr2 = pd.Series(['New York', 'Toronto', 'Lisbon', 'Rio'])

# Create the Index
index_ = ['City 1', 'City 3', 'City 4', 'City 5']

# set the index
sr2.index = index_

# Print the series
print(sr2)
