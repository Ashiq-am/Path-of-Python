import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Remove the first occurrence of the value 3
arr.remove(3)

print(arr)