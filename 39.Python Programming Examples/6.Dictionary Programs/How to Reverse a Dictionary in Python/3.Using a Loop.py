d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {}

# Loop through the dictionary and swap keys and values
for key, value in d1.items():
    d2[value] = key

print(d2)