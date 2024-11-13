# import counter class from collections module
from collections import Counter

# Creation of a Counter Class object using
# a string as an iterable data container
# Example - 1
a = Counter("geeksforgeeks")

# Elements of counter object
for i in a.elements():
    print(i, end=" ")
print()

# Example - 2
b = Counter({'geeks': 4, 'for': 1,
             'gfg': 2, 'python': 3})

for i in b.elements():
    print(i, end=" ")
print()

# Example - 3
c = Counter([1, 2, 21, 12, 2, 44, 5,
             13, 15, 5, 19, 21, 5])

for i in c.elements():
    print(i, end=" ")
print()

# Example - 4
d = Counter(a=2, b=3, c=6, d=1, e=5)

for i in d.elements():
    print(i, end=" ")
