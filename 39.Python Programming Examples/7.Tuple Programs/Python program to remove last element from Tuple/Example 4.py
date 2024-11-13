# create a list
tu = (1, 2, 3, 4, 5)

# remove last element
tu = list(tu)
tu.remove(tu[-1])
tu = tuple(tu)
print(tu)
