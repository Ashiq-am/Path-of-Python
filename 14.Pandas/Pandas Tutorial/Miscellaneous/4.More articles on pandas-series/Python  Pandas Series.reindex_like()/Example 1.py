# importing pandas as pd
import pandas as pd

# Creating the first Series
sr1 = pd.Series([10, 25, 3, 11, 24, 6])

# Create the Index
index_ = ['Coca Cola', 'Sprite', 'Coke', 'Fanta', 'Dew', 'ThumbsUp']

# set the index
sr1.index = index_

# Print the series
print(sr1)

# Creating the second Series
sr2 = pd.Series([10, 25, 3, 11, 24, 6, 25, 45])

# Create the Index
index_ = ['Coca Cola', 'Sprite', 'Coke', 'Fanta',
			'Dew', 'ThumbsUp', 'Mirinda', 'Appy']

# set the index
sr2.index = index_

# Print the series
print(sr2)
