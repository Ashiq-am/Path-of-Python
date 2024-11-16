# importing numpy module
import numpy as np

# create an array with integers with
# 6 rows and 2 columns
a = np.array([[1, 2], [5, 6], [9, 10, ],
			[78, 90], [4, 89], [56, 43]])
print(a)

# delete 0 th column
data = np.delete(a, 0, 1)
print("data after 0 th column deleted :", data)

# delete 1 st column
data = np.delete(a, 1, 1)
print("data after 1 st column deleted :", data)
