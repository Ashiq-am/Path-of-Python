# Python program to copy a nested list
import copy

# List initialization
Input = [[1, 0, 1], [1, 0, 1]]

# using deepcopy
Output = copy.deepcopy(Input)

# Printing
print("Initial list is:")
print(Input)
print("New assigned list is")
print(Output)
