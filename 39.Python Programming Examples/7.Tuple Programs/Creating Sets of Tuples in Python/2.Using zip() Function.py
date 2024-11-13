# Creating a set of tuples using the zip function
elements = [1, 2, 3, 4, 5]
squares = [x**2 for x in elements]

set_of_tuples = set(zip(elements, squares))

# Displaying the result
print(set_of_tuples)
