# Python3 code to demonstrate working of
# Find overlapping tuples from list
# Using list comprehension

# initialize list
test_list = [(4, 6), (3, 7), (7, 10), (5, 6)]

# initialize test tuple
test_tup = (1, 5)

# printing original list
print("The original list : " + str(test_list))

# Find overlapping tuples from list
# Using list comprehension
res = [(idx[0], idx[1]) for idx in test_list\
	if idx[0] >= test_tup[0] and idx[0] <= test_tup[1]\
	or idx[1] >= test_tup[0] and idx[1] <= test_tup[1]]

# printing result
print("The tuple elements that overlap the argument tuple is : "
													+ str(res))
