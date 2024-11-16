# 3-dimensional array
from pandas import np

array3D = np.array([[[ 0, 1, 2],
					[ 3, 4, 5],
					[ 6, 7, 8]],

					[[ 9, 10, 11],
					[12, 13, 14],
					[15, 16, 17]],

					[[18, 19, 20],
					[21, 22, 23],
					[24, 25, 26]]])

print(array3D)
print("shape :" +str(array3D.shape))

print("\nacessing element :" +str(array3D[0, 1, 0]))
print("acessing elements of a row and a column of an array:"
	+str(array3D[:, 1, 0]))
print("accessing sub part of an array :" +str(array3D[1]))
