# Python3 code to demonstrate working of
# Cross tuple summation grouping
# Using loop

# initializing list
test_list = [(4, 5), (7, 5), (8, 6), (10, 6), (10, 4), (6, 7), (3, 7)]

# printing original list
print("The original list is : " + str(test_list))

# Concatenate Similar Key values
# Using loop
temp = dict()
for ele1, ele2 in test_list:
	temp[ele2] = temp.get(ele2, 0) + ele1
res = [(ele2, ele1) for (ele1, ele2) in temp.items()]

# printing result
print("The grouped records are : " + str(res))
