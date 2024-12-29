import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Remove the element at index 2 and return it
val = arr.pop(2)

print(arr)
print(val)