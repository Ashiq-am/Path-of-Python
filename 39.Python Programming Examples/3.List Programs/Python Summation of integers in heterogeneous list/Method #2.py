# Python3 code to demonstrate working of
# Summation of integers in heterogeneous list
# using sum() + isinstance()

# initializing list
test_list = [5, 6, "gfg", 8, (5, 7), 'is', 9]

# printing original list
print("The original list is : " + str(test_list))

# Summation of integers in heterogeneous list
# using sum() + isinstance()
res = sum(filter(lambda i: isinstance(i, int), test_list))

# printing result
print("Summation of integers in list : " + str(res))
