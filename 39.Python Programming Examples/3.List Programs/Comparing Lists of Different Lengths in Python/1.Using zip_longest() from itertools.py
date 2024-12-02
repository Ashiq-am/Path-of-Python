from itertools import zip_longest

a = [1, 2, 3, 4]
b = [10, 20, 30]

for i, j in zip_longest(a, b, fillvalue=None):
    print(f"{i} vs {j}")