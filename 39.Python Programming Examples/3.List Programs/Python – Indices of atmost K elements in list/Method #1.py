# Python3 code to demonstrate
# Atmost K element indices
# using loop

# initializing list
test_list = [12, 11, 7, 15, 8, 18]

# printing original list
print("The original list : " + str(test_list))

# using loop
# Atmost K element indices
res = []
for idx in range(0, len(test_list)) :
	if test_list[idx] <= 11:
		res.append(idx)

# print result
print("The list of indices at most 11 : " + str(res))
