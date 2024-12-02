import array

# Create an array
arr = array.array('i', [1, 2, 3])

# Append elements using a loop
for i in range(4, 7):
    arr.append(i)

print(arr)
