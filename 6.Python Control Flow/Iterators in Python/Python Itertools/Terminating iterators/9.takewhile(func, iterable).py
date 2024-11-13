# Python code to demonstrate the working of
# takewhile()


import itertools

# initializing list
li = [2, 4, 6, 7, 8, 10, 20]

# using takewhile() to print values till condition is false.
print("The list values till 1st false value are : ", end="")
print(list(itertools.takewhile(lambda x: x % 2 == 0, li)))
