# range() function returns a range object.
# list() can convert this object to a list
a = list(range(3))
print(a)

# Convert a comprehension to list
b = list(x * x for x in range(5))
print(b)