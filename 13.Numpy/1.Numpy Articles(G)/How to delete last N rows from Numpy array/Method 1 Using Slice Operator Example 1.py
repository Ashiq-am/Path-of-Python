# importing numpy module
import numpy as np

# create an array with 6 rows and 3 columns
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],
			[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print(a)

# delete last 1 st row
print("data after deleting last one row ", a[:-1])

# delete last 2 nd row
print("data after deleting last two rows ", a[:-2])

# delete last 3 rd row
print("data after deleting last theww rows ", a[:-3])

# delete last 4 th row
print("data after deleting last four rows ", a[:-4])

# delete last 5 th row
print("data after deleting last five rows ", a[:-5])

# delete last 6 th row
print("data after deleting last six rows ", a[:-6])
