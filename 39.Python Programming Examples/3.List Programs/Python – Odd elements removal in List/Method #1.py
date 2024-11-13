# Python3 code to demonstrate
# Odd elements removal in List
# using naive method

# initializing list
test_list = [1, 9, 4, 7, 6, 5, 8, 3]

# printing original list
print ("The original list is : " + str(test_list))

# using naive method
# Odd elements removal in List
res = []
for val in test_list:
	if not (val % 2 != 0) :
		res.append(val)

# printing result
print ("List after removal of Odd values : " + str(res))
