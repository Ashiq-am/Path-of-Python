# Python3 code to demonstrate working of
# Dictionary Count in List
# Using list comprehension + isinstance()

# initializing list
test_list = [10, {'gfg' : 1}, {'ide' : 2, 'code' : 3}, 20]

# printing original list
print("The original list is : " + str(test_list))

# Dictionary Count in List
# Using list comprehension + isinstance()
res = len([ele for ele in test_list if isinstance(ele, dict)])

# printing result
print("The Dictionary count : " + str(res))
