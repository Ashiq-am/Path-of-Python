# Python3 code to demonstrate
# Integer count in Mixed List
# using lambda + map() + len() + isinstance()

# initializing list
test_list = [3, 'computer', 5, 'geeks', 6, 7]

# printing original list
print ("The original list is : " + str(test_list))

# using lambda + map() + len() + isinstance()
# Integer count in Mixed List
temp = list(map(lambda i: isinstance(i, int), test_list))
res = len([ele for ele in temp if ele])

# printing result
print ("The length of integers in list is : " + str(res))
