# Python3 code to demonstrate working of
# Test Kth index in Dictionary value list
# Using items() + loop

# initializing dictionary
test_dict = {'Gfg' : [1, 4, 8], 'is' : [8, 4, 2], 'best' : [7, 4, 9]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing K
K = 2

# initializing N
N = 4

# Test Kth index in Dictionary value list
# Using items() + loop
res = True
for key, val in test_dict.items():
	if val[K - 1] != N:
		res = False

# printing result
print("Are all Kth index equal to N : " + str(res))
