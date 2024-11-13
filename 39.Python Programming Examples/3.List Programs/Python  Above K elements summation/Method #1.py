# Python3 code to demonstrate
# Above K elements summation
# using loop

# initializing list
test_list = [12, 10, 18, 15, 8, 18]

# printing original list
print("The original list : " + str(test_list))

# using loop
# Above K elements summation
res = 0
for idx in range(0, len(test_list)) :
	if test_list[idx] > 10:
		res += test_list[idx]

# print result
print("The summation of elements greater than 10 : " + str(res))
