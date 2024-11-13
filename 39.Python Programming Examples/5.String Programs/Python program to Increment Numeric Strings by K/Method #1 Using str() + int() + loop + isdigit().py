# Python3 code to demonstrate working of
# Increment Numeric Strings by K
# Using str() + int() + loop + isdigit()

# initializing Matrix
test_list = ["gfg", "234", "is", "98", "123", "best", "4"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 6

res = []
for ele in test_list:

	# incrementing on testing for digit.
	if ele.isdigit():
		res.append(str(int(ele) + K))
	else:
		res.append(ele)

# printing result
print("Incremented Numeric Strings : " + str(res))
