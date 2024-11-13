# list -ve index slicing
l = ['a', 'b', 'c', 'd', 'e', 'f']
slice_obj = slice(-2, -6, -1)
print("list slicing:", l[slice_obj])

# string -ve index slicing
s = "geeks"
slice_obj = slice(-1)
print("string slicing:", s[slice_obj])

# tuple -ve index slicing
t = (1, 3, 5, 7, 9)
slice_obj = slice(-1, -3, -1)
print("tuple slicing:", t[slice_obj])
