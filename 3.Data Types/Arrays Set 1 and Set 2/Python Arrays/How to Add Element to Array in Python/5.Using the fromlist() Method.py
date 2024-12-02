import array

# Create an array
arr = array.array('i', [1, 2, 3])

# Append elements from a list using fromlist()
arr.fromlist([4, 5, 6])

print(arr)
