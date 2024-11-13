# Python3 code to demonstrate
# to get last element occurrence
# using max() + enumerate()

# initializing list
test_list = ['G', 'e', 'e', 'k', 's', 'f', 'o', 'r',
							'g', 'e', 'e', 'k', 's']

# using max() + enumerate()
# to get last element occurrence
res = max(idx for idx, val in enumerate(test_list)
									if val == 'e')

# printing result
print ("The index of last element occurrence: " + str(res))
