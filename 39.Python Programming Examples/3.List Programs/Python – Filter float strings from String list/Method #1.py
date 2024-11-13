# Python3 code to demonstrate working of
# Filter float strings from String list
# using loop + Exception Handling

# initialize list
test_list = ['gfg', '45.45', 'is', '87.5', 'best', '90.34']

# printing original list
print("The original list : " + str(test_list))

# Filter float strings from String list
# using loop + Exception Handling
res = []
for ele in test_list:
	try:
		float(ele)
	except ValueError:
		res.append(ele)

# printing result
print("String list after filtering floats : " + str(res))
