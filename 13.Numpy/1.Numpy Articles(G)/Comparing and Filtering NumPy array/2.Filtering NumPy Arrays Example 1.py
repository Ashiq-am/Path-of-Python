import numpy as np


a = np.array([1, 2, 3, 40, 50, 100,
			45, 87, 98])

# Taking a condition to filter the array
filter_ex = a < 16

# Creating new array using Condition.
new_arr = np.array([filter_ex])

# Printing new Array
print(*new_arr)
