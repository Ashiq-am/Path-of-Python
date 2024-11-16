# Importing Numpy module
import numpy as np

# Creating 3-D Numpy array
a1 = np.array([[[11, 25, 7], [30, 45, 55], [20, 45, 7]],
			[[50, 65, 8], [70, 85, 10], [11, 22, 33]],
			[[19, 69, 36], [1, 5, 24], [4, 20, 9]]])


print("Array 1 :")
print(a1)

# Creating 2-D array
a2 = np.array([[1, 15, 10],
			[6, 40, 50],
			[11, 5, 10]])

print("\nArray 2 :")
print(a2)

print("\nTake 1, 15, 10, 6, 40 and 50 from Array 2 and put them in 1st, 3rd, 5th, 9th, 11th and 15th positions of Array 1")

a1.put([0, 2, 4, 8, 10, 14], a2)

print("Resultant Array :")
print(a1)
