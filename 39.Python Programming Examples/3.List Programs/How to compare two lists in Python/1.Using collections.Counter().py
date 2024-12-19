import collections

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

# Counter creates a dictionary-like object
res = collections.Counter(a) == collections.Counter(b)
print(res)