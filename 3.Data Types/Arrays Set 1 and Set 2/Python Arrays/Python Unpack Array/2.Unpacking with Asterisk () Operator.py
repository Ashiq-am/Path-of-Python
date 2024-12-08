import array

arr = array.array('i', [1, 2, 3, 4, 5])
a, *rest, e = arr
print(a)     # 1
print(rest)  # [2, 3, 4]
print(e)     # 5