# Python code find whether a list
# exists in list of list.

# Input List Initialization
Input = [[1, 1, 1, 2], [2, 3, 4], [1, 2, 3], [4, 5, 6]]

# List to be searched
list_search = [4, 5, 6]

# Using any to find whether
# list exists or not
if any(list == list_search for list in Input):
    print("True")
else:
    print("False")

