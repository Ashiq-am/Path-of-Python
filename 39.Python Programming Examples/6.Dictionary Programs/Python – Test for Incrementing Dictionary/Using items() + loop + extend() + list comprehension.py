# Python3 code to demonstrate working of
# Test for Incrementing Dictionary
# Using extend() + list comprehension

# initializing dictionary
test_dict = {1: 2, 3: 4, 5: 6, 7: 8}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

temp = []

# forming list from dictionary
[temp.extend([key, val]) for key, val in test_dict.items()]

# checking for incrementing elements
res = True
for idx in range(0, len(temp) - 1):

	# test for increasing list
	if temp[idx + 1] - 1 != temp[idx]:
		res = False

# printing result
print("Is dictionary incrementing : " + str(res))
