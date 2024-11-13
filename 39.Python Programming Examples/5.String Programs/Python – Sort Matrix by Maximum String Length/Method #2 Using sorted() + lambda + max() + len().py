# Python3 code to demonstrate working of
# Sort Matrix by Maximum String Length
# Using sorted() + lambda + max() + len()

# initializing list
test_list = [['gfg', 'best'], ['geeksforgeeks'],
			['cs', 'rocks'], ['gfg', 'cs']]

# printing original list
print("The original list is : " + str(test_list))

# performing logic using lambda fnc.
res = sorted(test_list, key=lambda row: max([len(ele) for ele in row]))

# printing result
print("Sorted Matrix : " + str(res))
