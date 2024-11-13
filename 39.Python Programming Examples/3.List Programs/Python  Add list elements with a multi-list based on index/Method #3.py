# Python code to add list elements
# with a multi-list based on index

# List initialization
List = [1, 2, 3, 4, 5, 6]
List_of_List = [[0], [0, 1, 2], [0, 1], [0, 1], [0, 1, 2], [0]]
Output = []

# using zip
Output = [[z + x for z in y ]for x, y in
				zip(List, List_of_List)]

# Printing
print("Initial list is:", List)
print("Initial list of list is :", List_of_List)
print("Output is", Output)
