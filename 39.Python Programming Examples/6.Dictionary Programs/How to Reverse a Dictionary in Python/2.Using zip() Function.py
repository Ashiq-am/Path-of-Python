d1 = {'a': 1, 'b': 2, 'c': 3}

# Reverse the dictionary using zip
d2 = dict(zip(d1.values(), d1.keys()))

print(d2)