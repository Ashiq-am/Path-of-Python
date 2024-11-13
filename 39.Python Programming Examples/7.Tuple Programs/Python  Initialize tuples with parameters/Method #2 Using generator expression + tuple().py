# Python3 code to demonstrate working of
# Initialize tuples with parameters
# Using tuple() + generator expression

# Initializing size
N = 6

# Initializing default value
def_val = 2

# Initializing index to add value
idx = 3

# Initializing value to be added
val = 9

# Initialize tuples with parameters
# Using tuple() + generator expression
res = tuple(val if i == idx else def_val for i in range(N))

# printing result
print("The formulated tuple is : " + str(res))
