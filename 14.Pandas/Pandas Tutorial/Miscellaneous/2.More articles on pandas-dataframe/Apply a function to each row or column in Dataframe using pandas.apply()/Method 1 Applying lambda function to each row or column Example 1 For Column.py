# import pandas and numpy library
import pandas as pd
import numpy as np

# list of tuples
matrix = [(1,2,3,4),
		(5,6,7,8,),
		(9,10,11,12),
		(13,14,15,16)
		]

# Create a Dataframe object
df = pd.DataFrame(matrix, columns = list('abcd'))

# Applying a lambda function to each
# column which will add 10 to the value
new_df = df.apply(lambda x : x + 10)

# Output
new_df
