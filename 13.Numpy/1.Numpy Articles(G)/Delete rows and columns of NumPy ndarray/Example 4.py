# importing numpy module
import numpy as np

# create an array with integers
# with 3 rows and 3 columns
a = np.array([[67, 65, 45],
			[45, 67, 43],
			[3, 4, 5]])
print("Original\n", a)

# delete 1 st row and 2 nd
# row at a time
data = np.delete(a, [0, 1], 0)
print("data after 1 st and 2 ns row deleted :\n", data)
