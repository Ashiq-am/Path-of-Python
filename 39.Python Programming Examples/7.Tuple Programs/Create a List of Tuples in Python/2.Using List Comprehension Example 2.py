a = [[1, 'apple'], [2, 'orange'], [3, 'cherry']]

# List comprehension to create a list of tuples
a = [tuple(x) for x in a]
print(a)