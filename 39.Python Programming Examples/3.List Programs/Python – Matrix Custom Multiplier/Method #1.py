# Python3 code to demonstrate
# Matrix Custom Multiplier
# using loop + zip()

# Initializing list
test_list1 = [[1, 3], [5, 6], [8, 9]]
test_list2 = [4, 3, 6]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Matrix Custom Multiplier
# using loop + zip()
res = []
for mul, sub in zip(test_list2, test_list1):
	temp = []
	for ele in sub:
		temp.append(mul * ele)
	res.append(temp)

# printing result
print ("Matrix after custom multiplication : " + str(res))
