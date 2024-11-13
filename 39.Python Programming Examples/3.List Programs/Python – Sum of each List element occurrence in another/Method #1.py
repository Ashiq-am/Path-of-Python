# Python3 code to demonstrate
# Sum of each List element occurrence in another
# using nested loops

# Initializing lists
test_list1 = [1, 3, 4, 5, 1, 4, 4, 6, 7]
test_list2 = [4, 6, 1]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Sum of each List element occurrence in another
# using nested loops
res = 0
for ele in test_list2:
	for ele1 in test_list1:
		if ele1 == ele:
			res = res + 1

# printing result
print ("The occurrence count : " + str(res))
