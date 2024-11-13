# Python3 code to demonstrate
# to get last element occurrence
# using join() + rfind()

# initializing list
test_list = ['G', 'e', 'e', 'k', 's', 'f', 'o', 'r',
							'g', 'e', 'e', 'k', 's']

# using join() + rfind()
# to get last element occurrence
res = ''.join(test_list).rindex('e')

# printing result
print ("The index of last element occurrence: " + str(res))
