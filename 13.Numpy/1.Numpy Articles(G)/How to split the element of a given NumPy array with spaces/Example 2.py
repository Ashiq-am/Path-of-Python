import numpy as np


# Original Array
array = np.array(['Geeks For Geeks'], dtype=np.str)
print(array)

# Split the element of the said array
# with spaces
sparr = np.char.split(array)
print(sparr)
