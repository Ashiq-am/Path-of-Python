import array

# Create an array
arr = array.array('i', [1, 2, 3])

# Add multiple items using extend
arr.extend([4, 5, 6])

print(arr)