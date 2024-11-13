# Python3 code to demonstrate working of
# Initialize tuples with parameters
# Using tuple() + * operator

# Initializing size
N = 6

# Initializing default value
def_val = 2

# Initializing index to add value
idx = 3

# Initializing value to be added
val = 9

# Initialize tuples with parameters
# Using tuple() + * operator
res = [def_val] * N
res[idx] = val
res = tuple(res)

# printing result
print("The formulated tuple is : " + str(res))
