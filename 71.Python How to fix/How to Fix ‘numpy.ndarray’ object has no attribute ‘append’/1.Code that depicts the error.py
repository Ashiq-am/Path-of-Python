# Append method on python lists

import numpy
print("-"*15, "Python List", "-"*15)

# Create a python list
pylist = [1, 2, 3, 4]

# View the data type of the list object
print("Data type of python list:", type(pylist))

# Add (append) an item to the python list
pylist.append(5)

# View the items in the list
print("After appending item 5 to the pylist:", pylist)

print("-"*15, "Numpy Array", "-"*15)

# Append method on numpy arrays

# Import the numpy library

# Create a numpy array
nplist = numpy.array([1, 2, 3, 4])

# View the data type of the numpy array
print("Data type of numpy array:", type(nplist))

# Add (append) an item to the numpy array
nplist.append(5)
