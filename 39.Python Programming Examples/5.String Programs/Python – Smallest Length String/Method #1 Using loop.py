# Python3 code to demonstrate working of
# Smallest Length String
# using loop

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Smallest Length String
# using loop
min_len = 99999
for ele in test_list:
	if len(ele) < min_len:
		min_len = len(ele)
		res = ele

# printing result
print("Minimum length string is : " + res)
