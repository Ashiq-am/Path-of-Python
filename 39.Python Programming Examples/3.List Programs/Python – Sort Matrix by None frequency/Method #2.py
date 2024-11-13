# Python3 code to demonstrate working of
# Sort Matrix by None frequency
# Using sorted() + lambda

# initializing list
test_list = [[None, None, 4], [None, None, 3, None],
			[12, 4, 5], [None, 3, 4]]

# printing original list
print("The original list is : " + str(test_list))

# sorting using sorted()
# lambda function for None frequency logic
res = sorted(test_list, key=lambda row: len([ele for ele in row if not ele]))

# printing result
print("List after sorting : " + str(res))
