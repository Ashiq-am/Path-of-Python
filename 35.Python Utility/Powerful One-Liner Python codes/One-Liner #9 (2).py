import functools


n = 5
print(functools.reduce(lambda x, y: x * y, range(1, n + 1)))
