# Process utilizing asarray() function

# Import NumPy Library
import numpy as np

# Initialize our array
# Note, once again, that this is of type String
# Non-NumPy arrays can be used
initialArray = np.array(["1.1", "2.2", "3.3", "4.4"])

# Print our initial array
print("Our Initial Array: ", str(initialArray))
print("Original type: " + str(type(initialArray[0])))

# Actual conversion of array
# Note that we utilize np.float64 as the finalize data type
finalArray = np.asarray(initialArray, dtype = np.float64,
						order ='C')

# Print our converted array
print("Our Final Array: ", str(finalArray))
print("Final type: " + str(type(finalArray[0])))
