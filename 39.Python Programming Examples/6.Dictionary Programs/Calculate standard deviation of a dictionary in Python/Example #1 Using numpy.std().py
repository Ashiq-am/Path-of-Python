# imporitng numpy
import numpy as np

# creating our test dictionary
dicti = {'a': 20, 'b': 32, 'c': 12, 'd': 93, 'e': 84}

# declaring an empty list
listr = []

# appending all the values in the list
for value in dicti.values():
    listr.append(value)

# calculating standard deviation using np.std
std = np.std(listr)

# printing results
print(std)
