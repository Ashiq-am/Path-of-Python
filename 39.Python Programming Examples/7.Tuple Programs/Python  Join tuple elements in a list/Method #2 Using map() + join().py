# Python3 code to demonstrate
# joining tuple elements
# using join() + map()

# initializing tuple list
test_list = [('geeks', 'for', 'geeks'),
			('computer', 'science', 'portal')]

# printing original list
print ("The original list is : " + str(test_list))

# using join() + map()
# joining tuple elements
res = list(map(" ".join, test_list))

# printing result
print ("The joined data is : " + str(res))
