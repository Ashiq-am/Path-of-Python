# Python program to Create a
# Pandas DataFrame from a Numpy
# array and specify the index
# column and column headers

# import required libraries
import numpy as np
import pandas as pd

# creating a numpy array
numpyArray = np.array([[15, 22, 43],
					[33, 24, 56]])

# generating the Pandas dataframe
# from the Numpy array and specifying
# name of index and columns
panda_df = pd.DataFrame(data = numpyArray,
						index = ["Row_1", "Row_2"],
						columns = ["Column_1",
								"Column_2", "Column_3"])

# printing the dataframe
print(panda_df)
