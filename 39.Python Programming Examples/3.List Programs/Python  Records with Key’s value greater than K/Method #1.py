# Python3 code to demonstrate working of
# Records with Key's value greater than K
# Using loop

# Initialize list
test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6},
			{'it' : 5, 'is' : 7, 'best' : 8},
			{'CS' : 10, 'is' : 8, 'best' : 10}]

# Printing original list
print("The original list is : " + str(test_list))

# Initialize K
K = 6

# Using loop
# Records with Key's value greater than K
res = []
for sub in test_list:
	if sub['is'] >= K:
		res.append(sub)

# printing result
print("The filtered dictionary records is : " + str(res))
