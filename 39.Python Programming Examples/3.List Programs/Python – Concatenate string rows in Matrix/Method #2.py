# Python3 code to demonstrate
# Row String Concatenation Matrix
# using loop

# initializing list
test_list = [['gfg', ' is', ' best'], ['Computer', ' Science'], ['GeeksforGeeks']]

# printing original list
print("The original list : " + str(test_list))

# using loop
# Row String Concatenation Matrix
res = []
for sub in test_list:
	res_sub = ""
	for idx in sub:
		res_sub = res_sub + idx
	res.append(res_sub)

# print result
print("The row concatenation in matrix : " + str(res))
