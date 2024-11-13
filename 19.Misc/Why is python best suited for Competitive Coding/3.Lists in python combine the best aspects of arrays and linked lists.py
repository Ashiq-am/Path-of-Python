# Python code to demonstrate list operations
arr = [00, 11, 22, 33, 44, 55, 66, 77, 88, 99]

# deletion via index position
del arr[5]
print(arr)

# deletion via specifying particular element
arr.remove(22)
print(arr)

# insertion at any arbitrary position
arr[-1] = "A random number"
print(arr)

# concept of sub-lists
k = arr[:2]
print(k)
