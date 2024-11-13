# Python 3 code to demonstrate
# Unique values Multiplication
# using naive methods + loop

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

# using naive method + loop
# Unique values Multiplication
# from list
res = []
for i in test_list:
	if i not in res:
		res.append(i)
res = prod(res)

# printing list after product
print ("The unique elements product : " + str(res))
