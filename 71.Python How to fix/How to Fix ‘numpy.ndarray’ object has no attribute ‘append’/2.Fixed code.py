# Append method on numpy arrays

# Import the numpy library
import numpy

# Create a numpy array
nplist = numpy.array([1, 2, 3, 4])

# View the data type of the numpy array
print("Data type of numpy array:", type(nplist))

# View the items in the numpy array
print("Initial items in nplist:", nplist)

# Add (append) an item to the numpy array
nplist = numpy.append(nplist, 5)

# View the items in the numpy array
print("After appending item 5 to the nplist:", nplist)
