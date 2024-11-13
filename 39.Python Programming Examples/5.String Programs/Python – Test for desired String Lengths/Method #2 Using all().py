# Python3 code to demonstrate working of
# Test for desired String Lengths
# Using all()

# initializing string list
test_list = ["Gfg", 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# initializing Lengths list
len_list = [3, 2, 4, 3, 5]

# all() used to check for each element for length
res = all(len(test_list[idx]) == len_list[idx]
		for idx in range(len(test_list)))

# printing result
print("Are all strings of required lengths : " + str(res))
