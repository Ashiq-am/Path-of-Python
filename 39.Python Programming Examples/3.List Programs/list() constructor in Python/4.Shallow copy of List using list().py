a = [1, 2, 3]
a1 = list(a)

a1[0] = 5
print(a)   # Output: [1, 2, 3]

# different case for Nested List
b = [[1, 2, 3], [4, 5, 6]]
b1 = list(b)

# changing b1 will also reflect in b
b1[0][0] = 10
print(b)  # Output: [[10, 2, 3], [4, 5, 6]]