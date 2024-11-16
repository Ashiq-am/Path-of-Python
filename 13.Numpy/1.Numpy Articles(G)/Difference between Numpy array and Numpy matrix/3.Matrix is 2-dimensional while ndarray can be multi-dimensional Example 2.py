import numpy as np

arr1 = np.matrix([1, 2, 3])
print(arr1)
print("Dimensions:", arr1.ndim)
print("\n")

arr2 = np.matrix([[[1, 2], [3, 4]],
				[[5, 6], [7, 8]],
				[[9, 10], [11, 12]]])
print("2D array\n", arr2)
