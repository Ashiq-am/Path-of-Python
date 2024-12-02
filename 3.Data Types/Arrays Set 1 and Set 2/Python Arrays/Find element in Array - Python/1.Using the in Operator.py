import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Check if an item exists in the array
val = 3
if val in arr:
    print("Item found")
else:
    print(f"Not found")