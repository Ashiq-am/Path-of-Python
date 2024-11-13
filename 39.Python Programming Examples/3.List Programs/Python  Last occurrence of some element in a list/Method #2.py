# Python3 code to demonstrate
# to get last element occurrence
# using List Slice + index()

# initializing list
test_list = ['G', 'e', 'e', 'k', 's', 'f', 'o', 'r',
							'g', 'e', 'e', 'k', 's']

# using List Slice + index()
# to get last element occurrence
res = len(test_list) - 1 - test_list[::-1].index('e')

# printing result
print ("The index of last element occurrence: " + str(res))
