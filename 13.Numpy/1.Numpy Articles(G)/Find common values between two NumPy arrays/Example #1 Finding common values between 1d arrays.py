import numpy as np


# create 2 arrays
a = np.array([2, 4, 7, 1, 4])
b = np.array([7, 2, 9, 0, 5])

# Display the arrays
print("Original arrays", a, ' ', b)

# use the np.intersect1d method
c = np.intersect1d(a, b)

# Display result
print("Common values", c)
