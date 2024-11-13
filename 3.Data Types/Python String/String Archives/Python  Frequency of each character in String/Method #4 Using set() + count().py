# Python3 code to demonstrate
# each occurrence frequency using
# set() + count()

# initializing string
test_str = "GeeksforGeeks"

# using set() + count() to get count
# of each element in string
res = {i : test_str.count(i) for i in set(test_str)}

# printing result
print ("The count of all characters in GeeksforGeeks is :\n "
											+ str(res))
