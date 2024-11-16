# import pandas and numpy library
import pandas as pd
import numpy as np

# List of tuples
matrix = [(1,2,3,4),
		(5,6,7,8,),
		(9,10,11,12),
		(13,14,15,16)
		]

# Creating a Dataframe object
df = pd.DataFrame(matrix, columns = list('abcd'))

# Applying a numpy function to get t
# he sum of all values in each row
new_df = df.apply(np.sum, axis = 1)

# Output
new_df
