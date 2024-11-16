# Two dimensional numpy array
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]
arr = np.array([list_1, list_2, list_3])

# check size of the array
print("Size:", arr.size)

# check length of the array
print("Length:", len(arr))

# check shape of the array
print("Shape:", arr.shape)

# check dtype of the array elements
print("Datatype:", arr.dtype)

# change the dtype to 'float64'
arr = arr.astype('float64')
print(arr)
print(arr.dtype)

# convert array to list
lis = arr.tolist()
print("\nList:", lis)
print(type(lis))
