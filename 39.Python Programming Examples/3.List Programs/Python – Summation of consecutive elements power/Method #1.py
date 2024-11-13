# Python3 code to demonstrate working of
# Summation of consecutive elements power
# Using loop

# initializing list
test_list = [2, 2, 2, 3, 3, 3, 3, 4, 4, 5]

# printing original lists
print("The original list is : " + str(test_list))

freq = 1
res = 0
for idx in range(0, len(test_list) - 1):

	# adding powers
	if test_list[idx] != test_list[idx + 1]:
		res = res + test_list[idx] ** freq
		freq = 1
	else:
		freq += 1

# catering for last element
res = res + test_list[len(test_list) - 1] ** freq

# printing result
print("Computed summation of powers : " + str(res))
