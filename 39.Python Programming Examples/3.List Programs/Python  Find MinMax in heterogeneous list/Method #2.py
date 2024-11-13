# Python3 code to demonstrate
# Min / Max in heterogenous list
# using lambda + key + max()/min() + isinstance()

# initializing list
test_list = [3, 'computer', 5, 'geeks', 6, 7]

# printing original list
print ("The original list is : " + str(test_list))

# using lambda + key + max()/min() + isinstance()
# Min / Max in heterogenous list
res = max(test_list, key = lambda i: (isinstance(i, int), i))

# printing result
print ("The maximum value in list is : " + str(res))
