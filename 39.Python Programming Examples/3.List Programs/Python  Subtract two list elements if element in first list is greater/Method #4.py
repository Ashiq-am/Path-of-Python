# Python code to subtract if element in first
# list is greater than element in second list,
# else we output element of first list.


import numpy as np

# Input list initialisation
Input1 = np.array([10, 20, 30, 40, 50, 60])
Input2 = np.array([60, 50, 40, 30, 20, 10])

# using numpy
Output = np.where(Input1 >= Input2, Input1 - Input2, Input1)

# Printing output
print("Original list are :")
print(Input1)
print(Input2)

print("\nOutput list is")
print(Output)
