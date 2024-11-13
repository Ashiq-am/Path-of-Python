# importing the module
import statistics

# creating the test dictionary
dicti = {'a': 20, 'b': 32, 'c': 12, 'd': 93, 'e': 84}

# declaring an empty list
listr = []

# appending all the values in the list
for value in dicti.values():
	listr.append(value)

# Standard deviation of list
# Using pstdev()
res = statistics.pstdev(listr)
print(res)
