import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5, 3])

# Find all occurrences of an item
val = 3
idx = []

for i in range(len(arr)):
    if arr[i] == val:
        idx.append(i)

if idx:
    print(f"found at indices: {idx}.")
else:
    print("not found")