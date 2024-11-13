# code
import sys

d = {}
d['python'] = 1
for key in list(d.keys()):
    d.pop(key)

print(len(d))
print(sys.getsizeof(d))
