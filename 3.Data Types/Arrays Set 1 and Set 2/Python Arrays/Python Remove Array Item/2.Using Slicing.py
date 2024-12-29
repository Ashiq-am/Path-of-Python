import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Remove the element at index 2 (third element)
arr = arr[:2] + arr[3:]

print(arr)