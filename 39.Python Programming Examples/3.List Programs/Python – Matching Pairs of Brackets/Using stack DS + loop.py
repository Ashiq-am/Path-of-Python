# Python3 code to demonstrate working of
# Matching Pairs of Brackets
# Using stack DS + loop

# initializing list
test_list = [('(', 7), ('(', 9), (')', 10), (')', 11), ('(', 15), (')', 100)]

# printing original list
print("The original list is : " + str(test_list))

# Matching Pairs of Brackets
# Using stack DS + loop
stck = []
res = []
for ele1, ele2 in test_list:
	if '(' in ele1:
		stck.append((ele1, ele2))
	elif ')' in ele1:
		res.append((stck.pop()[1], ele2))

# printing result
print("The paired elements : " + str(res))
