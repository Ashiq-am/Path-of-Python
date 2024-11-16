# Importing libraries that will be used
import numpy as np

# Setting name of the file that the data is to be extarcted from in python
# This is a comma separated values file
filename = 'gfg_example2.csv'

# Loading file data into numpy array and storing it in variable.
# We use a delimiter that basically tells the code that at every ',' we encounter,
# we need to treat it as a new data point.
# The data type of the variables is set to be int using dtype parameter.
data_collected = np.loadtxt(filename, delimiter=',', dtype=int)

# Printing data stored
print(data_collected)


# Type of data
print(f'Stored in : {type(data_collected)} and data type is : {data_collected.dtype}')
