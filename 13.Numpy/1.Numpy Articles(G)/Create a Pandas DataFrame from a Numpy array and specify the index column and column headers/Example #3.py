# Python program to Create a
# Pandas DataFrame from a Numpy
# array and specify the index column
# and column headers

# import required libraries
import pandas as pd
import numpy as np

# creating a numpy array
numpyArray = np.array([[15, 22, 43],
					[33, 24, 56]])

# defining index for the
# Pandas dataframe
index = ['Row_' + str(i)
		for i in range(1, len(numpyArray) + 1)]

# defining column headers for the
# Pandas dataframe
columns = ['Column_' + str(i)
		for i in range(1, len(numpyArray[0]) + 1)]

# generating the Pandas dataframe
# from the Numpy array and specifying
# details of index and column headers
panda_df = pd.DataFrame(numpyArray ,
						index = index,
						columns = columns)

# printing the dataframe
print(panda_df)
