from scipy.special import cbrt

# cube root of elements in an array
arr = [64, 164, 564, 4, 640]
arr = list(map(cbrt,arr))
print(arr)
