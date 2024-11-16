# importing required librariess
import numpy as np

# creating a numpy array
array = np.array([['1', '2', '3','4','5'],
				['6', '7', '8','9','10'],
				['11', '12', '13','14','15']])

# convert nympy array to dictionary
d = dict(enumerate(array.flatten(), 1))

# print numpy array
print(array)
print(type(array))

# print dictionary
print(d)
print(type(d))
