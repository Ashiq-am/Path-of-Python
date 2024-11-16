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

# generating the Pandas dataframe
# from the Numpy array and specifying
# name of index and columns
panda_df = pd.DataFrame(data = numpyArray[0:, 0:],
						index = ['Row_' + str(i + 1)
						for i in range(numpyArray.shape[0])],
						columns = ['Column_' + str(i + 1)
						for i in range(numpyArray.shape[1])])

# printing the dataframe
print(panda_df)
