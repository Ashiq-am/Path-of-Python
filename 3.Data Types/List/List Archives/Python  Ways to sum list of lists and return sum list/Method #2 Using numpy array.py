# Python code to demonstrate
# sum of list of list
# using numpy array functions
import numpy as np

# Declaring initial list of list
List = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Printing list of list
print("Initial List - ", str(List))

# Using numpy sum
res = np.sum(List, 0)

# printing result
print("final list - ", str(res))
