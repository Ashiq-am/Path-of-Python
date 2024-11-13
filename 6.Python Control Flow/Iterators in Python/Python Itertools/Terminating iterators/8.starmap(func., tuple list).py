# Python code to demonstrate the working of
# starmap()


import itertools

# initializing tuple list
li = [(1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1)]

# using starmap() for selection value acc. to function
# selects min of all tuple values
print("The values acc. to function are : ", end="")
print(list(itertools.starmap(min, li)))
