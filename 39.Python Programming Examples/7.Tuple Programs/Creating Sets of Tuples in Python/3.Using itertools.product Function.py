import itertools

# Creating a set of tuples using itertools.product
elements = [1, 2, 3, 4, 5]

set_of_tuples = set(itertools.product(elements, repeat=2))

# Displaying the result
print(set_of_tuples)
