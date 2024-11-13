# Python3 code to demonstrate working of
# Check if tuple and list are identical
# Using all() + zip()

# Initializing list and tuple
test_list = ['gfg', 'is', 'best']
test_tup = ('gfg', 'is', 'best')

# printing original list and tuple
print("The original list is : " + str(test_list))
print("The original tuple is : " + str(test_tup))

# Check if tuple and list are identical
# Using all() + zip()
res = all( [i == j for i, j in zip(test_list, test_tup)] )

# printing result
print("Are tuple and list identical ? : " + str(res))
