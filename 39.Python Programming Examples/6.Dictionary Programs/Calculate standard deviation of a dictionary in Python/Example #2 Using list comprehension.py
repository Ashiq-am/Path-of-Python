# creating our test dictionary
dicti = {'a': 20, 'b': 32, 'c': 12, 'd': 93, 'e': 84}

# declaring an empty list
listr = []

# appending all the values in the list
for value in dicti.values():
	listr.append(value)

# Standard deviation of list
# Using sum() + list comprehension
mean = sum(listr) / len(listr)
variance = sum([((x - mean) ** 2) for x in listr]) / len(listr)
res = variance ** 0.5
print(res)
