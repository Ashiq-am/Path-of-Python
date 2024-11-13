# Given list of tuples
list_of_tuples = [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

# Unpacking tuples using zip
numbers, letters, booleans = zip(*list_of_tuples)

# Displaying the resulting lists
print("Numbers:", list(numbers))
print("Letters:", list(letters))
print("Booleans:", list(booleans))
