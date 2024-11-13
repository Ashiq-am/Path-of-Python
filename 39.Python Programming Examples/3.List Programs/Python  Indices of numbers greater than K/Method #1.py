# Python3 code to demonstrate
# index of matching element using loop

# initializing list
test_list = [12, 10, 18, 15, 8, 18]

# printing original list
print("The original list : " + str(test_list))

# using loop
# index of matching element
res = []
for idx in range(0, len(test_list)) :
	if test_list[idx] > 10:
		res.append(idx)

# print result
print("The list of indices greater than 10 : " + str(res))
