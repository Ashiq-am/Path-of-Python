import array

# Create an array
arr = array.array('i', [1, 2, 4, 5])

# Add an item at index 2 using slicing
arr[2:2] = array.array('i', [3])  # Convert the list to an array

print(arr)