a = [1, 2, 3]
a += list(map(lambda x: x + 4, range(3)))
print(a)