# Python program to Create a
# Pandas DataFrame from a Numpy
# array and specify the index column
# and column headers

# import required libraries
import pandas as pd
import numpy as np

# creating a numpy array and
# specifying the index and
# column headers along with
# data stored in the array
numpyArray = np.array([['', 'Column_1',
					'Column_2', 'Column_3'],
					['Row_1', 15, 22, 43],
					['Row_2', 33, 24, 56]])

# generating the Pandas dataframe
# from the Numpy array and specifying
# details of index and column headers
panda_df = pd.DataFrame(data = numpyArray[1:, 1:],
						index = numpyArray[1:, 0],
						columns = numpyArray[0, 1:])

# printing the dataframe
print(panda_df)
