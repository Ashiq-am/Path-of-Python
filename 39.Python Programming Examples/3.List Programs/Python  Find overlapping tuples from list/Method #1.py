# Python3 code to demonstrate working of
# Find overlapping tuples from list
# using loop

# initialize list
test_list = [(4, 6), (3, 7), (7, 10), (5, 6)]

# initialize test tuple
test_tup = (1, 5)

# printing original list
print("The original list : " + str(test_list))

# Find overlapping tuples from list
# using loop
res = []
for tup in test_list:
	if(tup[1]>= test_tup[0] and tup[0]<= test_tup[1]):
		res.append(tup)

# printing result
print("The tuple elements that overlap the argument tuple is : "
													+ str(res))
