# Python3 code to demonstrate working of
# Summation of tuple dictionary values
# Using tuple() + map() + values()

# Initializing dictionary
test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3, 2), 'best' : (1, 4, 9)}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Summation of tuple dictionary values
# Using tuple() + map() + values()
temp = []
for sub in test_dict.values():
	temp.append(list(sub))
res = tuple(map(sum, temp))

# printing result
print("The summation from each index is : " + str(res))
