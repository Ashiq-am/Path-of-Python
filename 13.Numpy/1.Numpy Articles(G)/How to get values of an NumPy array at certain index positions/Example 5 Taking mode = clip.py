# Importing Numpy module
import numpy as np

# Creating 2-D Numpy array
a1 = np.array([[11, 10, 22],
			[14, 58, 88]])

print("Array 1 :")
print(a1)

a2 = np.array([[1, 15, 6],
			[40, 50, 70]])

print("Array 2 :")
print(a2)

print("\nTake 1 and 15 from Array 2 and put them in 1st and 5th positions of Array 1")

print("by mistake we write the index which is out of bound, now mode will play its role")

a1.put([0, 15], a2, mode = 'clip')

print("\nResultant Array :")
print(a1)
