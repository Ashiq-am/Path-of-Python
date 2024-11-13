# Python code find whether a list
# exists in list of list.

# Input List Initialization
Input = [[1, 1, 1, 2], [2, 3, 4], [1, 2, 3], [4, 5, 6]]

# List to be searched
list_search = [1, 1, 1, 2]

# Using in to find whether
# list exists or not
if list_search in Input:
	print("True")
else:
	print("False")
