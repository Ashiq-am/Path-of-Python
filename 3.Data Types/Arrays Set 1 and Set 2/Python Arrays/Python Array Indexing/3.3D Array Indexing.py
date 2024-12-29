import array

# Creating a 3D array (array of arrays of arrays)
arr = array.array('i', [
    array.array('i', [array.array('i', [1, 2, 3]),
                      array.array('i', [4, 5, 6]),
                      array.array('i', [7, 8, 9])]),
    array.array('i', [array.array('i', [10, 11, 12]),
                      array.array('i', [13, 14, 15]),
                      array.array('i', [16, 17, 18])]),
])

# Accessing elements in the 3D array
print(arr[0][0][0])
print(arr[1][2][1])
print(arr[1][0][2])