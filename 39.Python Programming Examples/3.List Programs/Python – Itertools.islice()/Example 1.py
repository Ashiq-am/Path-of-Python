# Python program to demonstrate
# the working of islice

from itertools import islice

# Slicing the range function
for i in islice(range(20), 5):
    print(i)

li = [2, 4, 5, 7, 8, 10, 20]

# Slicing the list
print(list(itertools.islice(li, 1, 6, 2)))
