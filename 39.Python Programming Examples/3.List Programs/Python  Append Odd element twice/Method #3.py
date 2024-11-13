# Python code to create a new list from initial list
# with condition to append every odd element twice.

# Importing
import numpy as np

# List initialization
Input = [1, 2, 3, 8, 9, 11]
Output = []

# Using Numpy repeat
for x in Input:
	(Output.extend(np.repeat(x, 2, axis = 0))
	if x % 2 == 1 else Output.append(x))

# printing
print("Initial list is:'", Input)
print("New list is:", Output)
