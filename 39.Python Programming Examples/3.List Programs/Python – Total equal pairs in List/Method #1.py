# Python3 code to demonstrate working of
# Total equal pairs in List
# Using loop + count()

# initializing lists
test_list = [2, 4, 5, 2, 5, 4, 2, 4, 5, 7, 7, 8, 3]

# printing original list
print("The original list is : " + str(test_list))

all_ele = set(test_list)
res = 0
for ele in all_ele:

	# summing count from element list
	res += test_list.count(ele) // 2

# printing result
print("Total Pairs : " + str(res))
