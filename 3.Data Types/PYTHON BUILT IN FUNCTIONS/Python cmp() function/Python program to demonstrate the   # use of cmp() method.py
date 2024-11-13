# Python program to demonstrate the
# use of cmp() method

# when a<b
from filecmp import cmp

a = 1
b = 2
print(cmp(a, b))

# when a = b
a = 2
b = 2
print(cmp(a, b))

# when a>b
a = 3
b = 2
print(cmp(a, b))
