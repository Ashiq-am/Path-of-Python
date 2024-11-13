# Python3 code to demonstrate
# to find index of first element just
# greater than K
# using enumerate() + next()

# initializing list
test_list = [0.4, 0.5, 11.2, 8.4, 10.4]

# printing original list
print ("The original list is : " + str(test_list))

# using enumerate() + next() to find index of
# first element just greater than 0.6
res = next(x for x, val in enumerate(test_list)
								if val > 0.6)

# printing result
print ("The index of element just greater than 0.6 : "
										+ str(res))
