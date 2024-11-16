# Importing libraries that will be used
import numpy as np

# Setting name of the file that the data is to be extarcted from in python
filename = 'gfg_example1.txt'

# Loading file data into numpy array and storing it in variable called data_collected
data_collected = np.loadtxt(filename)

# Printing data stored
print(data_collected)


# Type of data
print(
	f'Stored in : {type(data_collected)} and data type is : {data_collected.dtype}')
