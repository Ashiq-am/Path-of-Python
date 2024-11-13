from scipy.spatial.distance import cdist

arr1 = [[1, 3, 27],
        [3, 4, 6],
        [7, 6, 3],
        [3, 6, 8]]

print("Value of cdist is :", cdist(arr1, arr1))
