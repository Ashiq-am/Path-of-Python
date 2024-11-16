# Copying Numpy array with normal assignment
nc = arr

# both arr and nc have same id
print("Normal Assignment copy")
print("id of arr:", id(arr))
print("id of nc:", id(nc))

# updating nc
nc[0]= 12

# printing the values
print("original array:", arr)
print("assigned array:", nc)
