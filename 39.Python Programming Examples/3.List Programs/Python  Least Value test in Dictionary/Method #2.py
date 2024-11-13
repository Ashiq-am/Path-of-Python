# Python3 code to demonstrate working of
# Least Value test in Dictionary
# Using loop

# Initialize dictionary
test_dict = {'gfg' : 8, 'is' : 10, 'best' : 11}

# Printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Initialize K
K = 8

# using loop
# Least Value test in Dictionary
res = True
for key in test_dict:
	if test_dict[key] < K:
		res = False

# printing result
print("Does all keys have atleast K value ? : " + str(res))
