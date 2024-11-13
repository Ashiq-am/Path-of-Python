# Python 3 code to demonstrate
# Index Value Summation List
# using naive method

# initializing list
test_list = [1, 4, 5, 6, 7]

# Printing list
print ("The original list is : " + str(test_list))

# using naive method to
# Index Value Summation List
res = []
for i in range(len(test_list)):
	res.append(i + test_list[i])

print ("The list index-value summation is : " + str(res))
