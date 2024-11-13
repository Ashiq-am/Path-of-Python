s1 = {2, 5, 3, 7, 'c', 'a', 8}
s2 = {3, 7, 8, 'c', 9, 11, 'd'}

# union
w = s1 | s2

# intersection
x = s1 & s2

# elements which are in s1 but not in s2
# and elements which are in s2 but not in s1
y = s1 ^ s2

# set difference
z = s1-s2
print(w)
print(x)
print(y)
print(z)
