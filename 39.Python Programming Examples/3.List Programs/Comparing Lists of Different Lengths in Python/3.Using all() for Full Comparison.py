a = [1, 2, 3, 4]
b = [1, 2, 3]

is_equal = all(a == b for a, b in zip(a, b))
print(is_equal)