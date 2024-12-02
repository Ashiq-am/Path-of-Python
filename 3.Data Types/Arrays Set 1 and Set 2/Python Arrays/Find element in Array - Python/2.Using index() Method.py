import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Find the index of an item
try:
    val = 4
    idx = arr.index(val)
    print(f"found at index {idx}.")
except ValueError:
    print("not found")