# Original array
arr = array.array('i', [1, 2, 3, 4, 5])

# Update the elements at indices 1 to 3 (second to fourth elements)
arr[1:4] = array.array('i', [20, 30, 40])
print(arr)