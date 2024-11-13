#above code with map, filter and lambda

# Declare a list
x = [2, 3, 4, 5, 6]

# Perform the same operation as in above post
y = map(lambda v : v * 5, filter(lambda u : u % 2, x))
print(y)
