import array

# Create two arrays
arr1 = array.array('i', [1, 2, 3])
arr2 = array.array('i', [4, 5, 6])

# Concatenate using the + operator
arr = arr1 + arr2

print(arr)