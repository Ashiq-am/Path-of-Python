from itertools import zip_longest

# Given list of tuples with different lengths
list_of_tuples = [(1, 'a'), (2, 'b', True), (3, 'c', False, 'extra')]

# Unpacking tuples using zip_longest to handle different lengths
numbers, letters, booleans, * \
	extra = zip_longest(*list_of_tuples, fillvalue=None)

# Displaying the resulting lists
print("Numbers:", list(numbers))
print("Letters:", list(letters))
print("Booleans:", list(booleans))
print("Extra:", extra)
