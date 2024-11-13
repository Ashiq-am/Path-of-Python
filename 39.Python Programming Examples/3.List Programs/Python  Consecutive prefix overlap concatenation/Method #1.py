# Python3 code to demonstrate working of
# Consecutive prefix overlap concatenation
# Using endswith() + join() + list comprehension + zip() + loop

def help_fnc(i, j):
	for ele in range(len(j), -1, -1):
		if i.endswith(j[:ele]):
			return j[ele:]

# initializing list
test_list = ["gfgo", "gone", "new", "best"]

# printing original list
print("The original list is : " + str(test_list))

# Consecutive prefix overlap concatenation
# Using endswith() + join() + list comprehension + zip() + loop
res = ''.join(help_fnc(i, j) for i, j in zip([''] +
						test_list, test_list))

# printing result
print("The resultant joined string : " + str(res))
