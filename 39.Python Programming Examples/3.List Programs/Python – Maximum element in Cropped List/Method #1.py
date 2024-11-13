# Python3 code to demonstrate
# Maximum element in Cropped List
# using loop + max()

# initializing list
test_list = [2, 3, 5, 7, 9, 10, 8, 6]

# printing original list
print ("The original list is : " + str(test_list))

i, j = 2, 5

# Maximum element in Cropped List
# using loop + max()
res = []
for idx, ele in enumerate(test_list):
	if idx >= i and idx < j:
		res.append(ele)
res = max(res)

# printing result
print ("The maximum element in range is : " + str(res))
