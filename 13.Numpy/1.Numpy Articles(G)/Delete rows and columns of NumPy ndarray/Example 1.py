# importing numpy module
import numpy as np

# create an array with integers
# with 3 rows and 4 columns
a = np.array([[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12]])
print(a)

# delete 0 th row
data = np.delete(a, 0, 0)
print("data after 0 th row deleted :", data)

# delete 1 st row
data = np.delete(a, 1, 0)
print("data after 1 st row deleted :", data)

# delete 2 nd row
data = np.delete(a, 2, 0)
print("data after 2 nd row deleted :", data)
