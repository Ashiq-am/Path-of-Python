arr = array.array('i', [1, 2, 3])
arr.append(4)
print(arr)

arr.insert(2, 10)  # Insert 10 at index 2
print(arr)

arr.remove(3)  # Removes the first occurrence of 3
print(arr)

val = arr.pop(1)  # Remove and return the element at index 1
print(val)
print(arr)