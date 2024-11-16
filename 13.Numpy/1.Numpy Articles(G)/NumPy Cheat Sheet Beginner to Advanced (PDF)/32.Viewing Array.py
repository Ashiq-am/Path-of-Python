# Creating a view of a
# NumPy array
# creating view
v = arr.view()

# both arr and v have different id
print("id of arr:", id(arr))
print("id of v:", id(v))

# changing original array
# will effect view
arr[0] = 12

# printing array and view
print("original array:", arr)
print("view:", v)
