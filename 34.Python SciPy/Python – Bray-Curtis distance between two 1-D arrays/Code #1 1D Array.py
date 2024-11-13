from scipy.spatial.distance import braycurtis

a = [3, 1]

b = [2, 1]
arr1 = braycurtis(a, b)

print("Value of braycurtis is :", arr1)
