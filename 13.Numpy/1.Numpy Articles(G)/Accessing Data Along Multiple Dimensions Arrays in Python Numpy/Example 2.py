# 2-dimensional array
from pandas import np

array2D = np.array([[93, 95],
					[84, 100],
					[99, 87]])

print(array2D)
print("shape :" +str(array2D.shape))

print("\npositive indexing :" +str(array2D[1, 0]))
print("negative indexing :" +str(array2D[-2, 0]))

print("\nslicing using positive indices :" +str(array2D[0:3, 1]))
print("slicing using positive indices :" +str(array2D[:, 1]))
print("slicing using negative indices :" +str(array2D[:, -1]))
