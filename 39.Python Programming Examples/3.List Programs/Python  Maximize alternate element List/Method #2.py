# Python3 code to demonstrate
# Maximize alternate element List
# using loop

# initializing list
test_list = [2, 1, 5, 6, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# using loop
# Maximize alternate element List
res = [0, 0]
for i in range(0, len(test_list)):
	if(i % 2):
		res[1] = max(res[1], test_list[i])
	else :
		res[0] = max(res[0], test_list[i])

# print result
print("The alternate elements maximum list : " + str(res))
