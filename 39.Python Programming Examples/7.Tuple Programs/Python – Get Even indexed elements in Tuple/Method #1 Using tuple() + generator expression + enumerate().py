# Python3 code to demonstrate working of
# Extract Even indexed elements in Tuple
# Using tuple() + generator expression + enumerate()

# initializing tuples
test_tuple = (5, 'Gfg', 2, 8.8, 1.2, 'is')

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Extract Even indexed elements in Tuple
# Using tuple() + generator expression + enumerate()
res = tuple(ele for idx, ele in enumerate(test_tuple) if idx % 2 == 0)

# printing result
print("The even indexed elements : " + str(res))
