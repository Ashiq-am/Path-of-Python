# importing pandas as pd
import pandas as pd

# Creating the first Series
sr1 = pd.Series([80, 25, 3, 25, 24, 6])

# Creating the second Series
sr2 = pd.Series([80, 25, 3, 80, 24, 25])

# Create the Index
index_ = ['Coca Cola', 'Sprite', 'Coke', 'Fanta', 'Dew', 'ThumbsUp']

# set the first series index
sr1.index = index_

# set the second series index
sr2.index = index_

# Print the first series
print(sr1)

# Print the second series
print(sr2)
