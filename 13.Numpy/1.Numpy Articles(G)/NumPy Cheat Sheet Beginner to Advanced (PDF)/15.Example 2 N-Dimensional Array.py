# Adding the values at the end
# of a numpy array
arr = np.arange(1, 13).reshape(2, 6)
print("Original Array")
print(arr, "\n")

# create another array which is
# to be appended column-wise
col = np.arange(5, 11).reshape(1, 6)
arr_col = np.append(arr, col, axis=0)
print("Array after appending the values column wise")
print(arr_col, "\n")

# create an array which is
# to be appended row wise
row = np.array([1, 2]).reshape(2, 1)
arr_row = np.append(arr, row, axis=1)
print("Array after appending the values row wise")
print(arr_row)
