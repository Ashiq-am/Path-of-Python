# Importing libraries that will be used
import numpy as np

# Setting name of the file that the data is to be extarcted from in python
filename = 'gfg_example4.csv'

# Loading file data into numpy array and storing it in variable called data_collected
data_collected = np.loadtxt(
	filename, skiprows=1, usecols=[0, 1], delimiter=',')

# Printing data stored
print(data_collected)


# Type of data
print(f'Stored in : {type(data_collected)} and data type is : {data_collected.dtype}')
