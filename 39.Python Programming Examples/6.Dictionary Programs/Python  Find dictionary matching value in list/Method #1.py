# Python3 code to demonstrate working of
# Find dictionary matching value in list
# Using loop

# Initialize list
test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6},
			{'it' : 5, 'is' : 7, 'best' : 8},
			{'CS' : 10}]

# Printing original list
print("The original list is : " + str(test_list))

# Using loop
# Find dictionary matching value in list
res = None
for sub in test_list:
	if sub['is'] == 7:
		res = sub
		break

# printing result
print("The filtered dictionary value is : " + str(res))
