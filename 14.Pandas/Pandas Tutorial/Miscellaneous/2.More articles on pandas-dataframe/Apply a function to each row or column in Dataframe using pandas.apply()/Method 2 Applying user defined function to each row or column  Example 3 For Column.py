# function to returns x+y
def addData(x, y):
	return x + y

# import pandas and numpy library
import pandas as pd
import numpy as np

# list of tuples
matrix = [(1,2,3,4),
		(5,6,7,8,),
		(9,10,11,12),
		(13,14,15,16)
		]

# Creating a Dataframe object
df = pd.DataFrame(matrix, columns = list('abcd'))

# Appling a user defined function to each
# column which will add value in each
# column by given number
new_df = df.apply(addData, args = [1])

# Output
print(new_df)
