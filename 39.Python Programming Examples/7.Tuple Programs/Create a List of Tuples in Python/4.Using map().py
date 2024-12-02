a = [[1, 'apple'], [2, 'orange'], [3,'cherry']]

# Using map to convert each list to a tuple
b = list(map(tuple, a))

print(b)