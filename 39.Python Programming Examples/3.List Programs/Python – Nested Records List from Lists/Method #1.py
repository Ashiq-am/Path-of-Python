# Python3 code to demonstrate working of
# Nested Records List from Lists
# Using zip() + loop

# initializing lists
test_list1 = ['gfg', 'best']
test_list2 = [[1, 2], [3, 4]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# initializing add_key
add_key = 'id'

# Nested Records List from Lists
# Using zip() + loop
res = dict()
for key, val in zip(test_list1, test_list2):
	res[key]=[{add_key : idx} for idx in val]

# printing result
print("The constructed dictionary is : " + str(res))
