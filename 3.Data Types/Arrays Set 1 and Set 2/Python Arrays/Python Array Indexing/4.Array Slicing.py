import array

# Create an array of integers
arr= array.array('i', [10, 20, 30, 40, 50, 60, 70])

# Slice the array
print(arr[1:5])
print(arr[::2])
print(arr[-4:-1])