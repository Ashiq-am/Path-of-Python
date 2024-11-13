# Python3 code to demonstrate working of
# Sort Dictionaries by Size
# Using sorted() + len() + lambda

# initializing list
test_list = [{4: 6, 9: 1, 10: 2, 2: 8}, {
	4: 3, 9: 1}, {3: 9}, {1: 2, 9: 3, 7: 4}]

# printing original lists
print("The original list is : " + str(test_list))

# performing sort using sorted(), lambda for filtering
res = sorted(test_list, key=lambda sub: len(sub))

# printing result
print("Sorted List : " + str(res))
