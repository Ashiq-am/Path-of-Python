# Using list() to create a single-item list from a tuple
a = list((5,))
print(a)
print(type(a))

# Using list() to create a list from a single-character string
a = list("A")
print(a)
print(type(a))

# Below code would not work as we need an iterable
# a = list(5)
# a = list(True)

# note - int and bool object are not iterable