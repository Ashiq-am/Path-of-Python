# Python3 code to demonstrate working of
# Substitute K for first occurrence of elements
# Using loop

# initializing list
test_list = [4, 3, 3, 7, 8, 7, 4, 6, 3]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 10

# Substitute K for first occurrence of elements
# Using loop
lookp = set()
res = []
for ele in test_list:
	if ele not in lookp:
		lookp.add(ele)
		res.append(K)
	else:
		res.append(ele)

# printing result
print("List after Substitution : " + str(res))
