from itertools import starmap

pairs = [(1, 2), (3, 4), (5, 6)]

def add(a, b):
    return a + b

results = starmap(add, pairs)

for result in results:
    print(result)
