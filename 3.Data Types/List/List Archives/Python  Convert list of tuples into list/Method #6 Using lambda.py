# Python code to convert list of tuple into list


# List of tuple initialization
tup = [(1, 2), (3, 4), (5, 6)]

# Using map for 0 index
b = map(lambda x: x[0], tup)

# Using map for 1 index
c = map(lambda x: x[1], tup)

# converting to list
b = list(b)
c = list(c)

# Combining output
out = b + c

# printing output
print(out)
