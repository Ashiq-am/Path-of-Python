# Importing libraries that will be used
import numpy as np

# Setting name of the file that the data is to be extarcted from in python
# This
filename = 'gfg_example3.tsv'

# Loading file data into numpy array and storing it in variable called data_collected
# We use a delimiter that basically tells the code that at every ',' we encounter,
# we need to treat it as a new data point.
data_collected = np.loadtxt(filename, delimiter='\t')

# Printing data stored
print(data_collected)


# Type of data
print(f'Stored in : {type(data_collected)} and data type is : {data_collected.dtype}')
