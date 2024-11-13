# initializing list
test_list = [[4, 5, 1, 7], [6, 5], [9, 8, 2], [7, 1]]

# printing original list
print("The original list is : " + str(test_list))

# initializing custom list
cus_list = [4, 5, 7]

# performing sort using sorted()
res = sorted(test_list, key=lambda sub: len(
	[ele for ele in sub if ele in cus_list]))

# printing result
print("Sorted Matrix : " + str(res))
