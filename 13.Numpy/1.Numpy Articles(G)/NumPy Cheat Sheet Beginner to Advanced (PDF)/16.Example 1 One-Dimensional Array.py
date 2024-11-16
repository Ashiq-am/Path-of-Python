arr = np.asarray([1, 2, 3, 4])
# Python Program illustrating numpy.insert()
print("1D arr:", arr)
print("Shape:", arr.shape)

# Inserting value 9 at index 1
a = np.insert(arr, 1, 9)
print("\nArray after insertion:", a)
print("Shape:", a.shape)
