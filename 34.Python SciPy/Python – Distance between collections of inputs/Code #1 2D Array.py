from scipy.spatial.distance import cdist
a = [[1, 3, 27], [3, 6, 8]]
arr1 = cdist(a, a)

print("Value of cdist is :", arr1)
