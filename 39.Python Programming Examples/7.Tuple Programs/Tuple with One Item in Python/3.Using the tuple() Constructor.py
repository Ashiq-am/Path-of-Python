# Using tuple() with a single-item list
t = tuple([5])
print(t)
print(type(t))

# using a string iterable inside tuple() constructor
t = tuple("A")
print(t)
print(type(t))

# Below code would not work as integer is not iterable
# t = tuple(5)