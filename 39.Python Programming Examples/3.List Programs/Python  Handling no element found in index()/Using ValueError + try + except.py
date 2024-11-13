# Python3 code to demonstrate working of
# Handling no element found in index()
# Using try + except + ValueError

# initializing list
test_list = [6, 4, 8, 9, 10]

# printing list
print("The original list : " + str(test_list))

# Handling no element found in index()
# Using try + except + ValueError
try :
	test_list.index(11)
	res = "Element found"
except ValueError :
	res = "Element not in list !"

# Printing result
print("The value after catching error : " + str(res))
