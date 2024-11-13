# Python3 code to demonstrate working of
# String concatenation in Heterogenous list
# using join() + isinstance()

# initializing list
test_list = [5, 6, "gfg ", 8, (5, 7), ' is', 9, ' best']

# printing original list
print("The original list is : " + str(test_list))

# String concatenation in Heterogenous list
# using join() + isinstance()
res = "".join(filter(lambda i: isinstance(i, str), test_list))

# printing result
print("Concatenation of strings in list : " + str(res))
