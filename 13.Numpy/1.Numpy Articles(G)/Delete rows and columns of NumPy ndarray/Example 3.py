# importing numpy module
import numpy as np

# create an array with integers
# with 3 rows and 3 columns
a = np.array([[67, 65, 45],
			[45, 67, 43],
			[3, 4, 5]])
print("Original\n", a)

# delete 1 st row
data = np.delete(a, 0, 0)
print("data after 1 st row deleted :\n", data)

# delete 1 st column
data = np.delete(a, 0, 1)
print("data after 1 st column deleted :\n", data)
