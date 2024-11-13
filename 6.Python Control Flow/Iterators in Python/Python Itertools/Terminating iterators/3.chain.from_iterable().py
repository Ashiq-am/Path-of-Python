# Python code to demonstrate the working of
# chain.from_iterable()


import itertools

# initializing list 1
li1 = [1, 4, 5, 7]

# initializing list 2
li2 = [1, 6, 5, 9]

# initializing list 3
li3 = [8, 10, 5, 4]

# intializing list of list
li4 = [li1, li2, li3]

# using chain.from_iterable() to print all elements of lists
print("All values in mentioned chain are : ", end="")
print(list(itertools.chain.from_iterable(li4)))
