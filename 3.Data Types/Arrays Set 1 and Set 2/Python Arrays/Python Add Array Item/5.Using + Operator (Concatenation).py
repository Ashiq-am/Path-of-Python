import array

# Create an array
arr = array.array('i', [1, 2, 3])

# Add an item using concatenation
arr = arr + array.array('i', [4])

print(arr)