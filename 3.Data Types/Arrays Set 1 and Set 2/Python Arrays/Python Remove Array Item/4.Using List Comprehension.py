import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 2, 4, 2, 5])

# Remove all occurrences of the value 2
arr = array.array('i', [x for x in arr if x != 2])

print(arr)