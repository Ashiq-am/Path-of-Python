import itertools

input = [1, 2, 3, 4, 5]
key = 7

result = list(itertools.chain(*[[ele, key] for ele in input]))

print(result)
