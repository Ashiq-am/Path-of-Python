import copy

d1 = {'a': 1, 'b': {'x': 10, 'y': 20}, 'c': 3}
d2 = copy.deepcopy(d1)

# Modify a nested dictionary
d2['b']['x'] = 99

print(d1)
print(d2)