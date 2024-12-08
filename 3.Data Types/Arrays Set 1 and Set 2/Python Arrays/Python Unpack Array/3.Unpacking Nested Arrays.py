import array

arr1 = array.array('i', [1, 2])
arr2 = array.array('i', [3, 4])
arr3 = [arr1, arr2]

(a, b), (c, d) = arr3
print(a, b)  # 1 2
print(c, d)  # 3 4