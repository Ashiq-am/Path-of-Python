# importing pandas as pd
import pandas as pd

# Creating the first Series
sr1 = pd.Series([51, 10, 24, 18, None, 84, 12, 10, 5, 24, 2])

# Creating the second Series
sr2 = pd.Series([11, 21, 8, 18, 65, 18, 32, 10, 5, 32, None])

# Create the Index
index_ = pd.date_range('2010-10-09', periods = 11, freq ='M')

# set the first index
sr1.index = index_

# set the second index
sr2.index = index_

# Print the first series
print(sr1)

# Print the second series
print(sr2)
