# Python3 code to demonstrate working of
# Sort by Rear Character in Strings List
# Using sort()

# sort key fnction
def get_rear(sub):
	return sub[-1]

# initializing list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# using sort with key fnc.
# performs inplace sort
test_list.sort(key = get_rear)

# printing result
print("Sorted List : " + str(test_list))
