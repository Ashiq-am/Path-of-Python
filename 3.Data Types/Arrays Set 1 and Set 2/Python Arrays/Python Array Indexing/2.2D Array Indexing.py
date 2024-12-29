import array

# Creating a 2D array (array of arrays)
arr = array.array('i', [array.array('i', [1, 2, 3]),
                                array.array('i', [4, 5, 6]),
                                array.array('i', [7, 8, 9])])

# Accessing elements in the 2D array
print(arr[0][0])  # (first element of first row)
print(arr[1][2])  # (third element of second row)
print(arr[2][1])  # (second element of third row)