import array

# Create an array
arr = array.array('i', [1, 2, 3])

# Concatenate arrays
arr = arr + array.array('i', [4, 5])

print(arr)
