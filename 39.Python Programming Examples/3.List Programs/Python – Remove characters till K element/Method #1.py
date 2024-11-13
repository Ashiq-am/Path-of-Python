# Python3 code to demonstrate
# Remove characters till K element
# using loop

# Initializing list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 'best'

# Remove characters till K element
# using loop
res = []
flag = 0
for ele in test_list:
	if ele == K:
		flag = 1
		continue
	if flag:
		res.append(ele)

# printing result
print ("List elements after removing all before K : " + str(res))
