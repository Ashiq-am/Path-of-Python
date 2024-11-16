# Python code to demonstrate
# to replace negative values with 0
import numpy as np

ini_array1 = np.array([1, 2, -3, 4, -5, -6])

# printing initial arrays
print("initial array", ini_array1)

# code to replace all negative value with 0
result = np.where(ini_array1<0, 0, ini_array1)

# printing result
print("New resulting array: ", result)
