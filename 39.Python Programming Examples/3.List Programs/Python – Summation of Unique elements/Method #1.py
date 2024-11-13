# Python 3 code to demonstrate
# Summation of Unique elements
# using naive methods + sum()

# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

# using naive method + sum()
# Summation of Unique elements
# from list
res = []
for i in test_list:
	if i not in res:
		res.append(i)
res = sum(res)

# printing list after removal
print ("The unique elements summation : " + str(res))
