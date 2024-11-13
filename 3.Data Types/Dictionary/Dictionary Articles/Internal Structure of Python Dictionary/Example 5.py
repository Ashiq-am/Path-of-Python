import sys

d = {}
d['python'] = 1
for key in list(d.keys()):
    d.pop(key)

print(len(d))
d.clear()
print(sys.getsizeof(d))
