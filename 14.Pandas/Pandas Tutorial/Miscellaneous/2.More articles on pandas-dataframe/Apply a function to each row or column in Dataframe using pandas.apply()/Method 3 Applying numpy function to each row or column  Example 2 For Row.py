# import pandas and numpy library
import pandas as pd
import numpy as np

# List of tuples
matrix = [(1,2,3,4),
		(5,6,7,8,),
		(9,10,11,12),
		(13,14,15,16)
		]

# Creating a dataframe object
df = pd.DataFrame(matrix, columns = list('abcd'))

# Apply a numpy function to each row
# to find square root of each value
new_df = df.apply(np.sqrt, axis = 1)

# Output
new_df
