arr = np.asarray([1, 2, 3, 4])
# check size of the array
print("Size:", arr.size)

# check len of the array
print("len:", len(arr))

# check shape of the array
print("Shape:", arr.shape)

# check dtype of the array elements
print("Datatype:", arr.dtype)

# change the dtype to 'float64'
arr = arr.astype('float64')
print(arr)
print("Datatype:", arr.dtype)

# convert array to list
lis = arr.tolist()
print("\nList:", lis)
print(type(lis))
