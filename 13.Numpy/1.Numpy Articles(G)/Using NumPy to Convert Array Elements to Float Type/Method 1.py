# Process utilizing astype() function

# Import NumPy Library
import numpy as np

# Initialize our Array with Strings
# The String Type is denoted by the quotes ""
initialArray = ["1.1", "2.2", "3.3", "4.4"]

# Convert initial Array to NumPy Array
# Use the array() function
sampleArray = np.array(initialArray)

# Print our Initial Array
print("Our initial array: ", str(initialArray))
print("Original type: " + str(type(initialArray[0])))

# Actual Conversion of Array
# Note usage of astype() function
# np.float can be changed to represent differing types
convertedArray = sampleArray.astype(np.float)

# Print our final result
# Note that usage of str() is due to Python conventions
print("Our final array: ", str(convertedArray))
print("Final type: " + str(type(convertedArray[0])))
