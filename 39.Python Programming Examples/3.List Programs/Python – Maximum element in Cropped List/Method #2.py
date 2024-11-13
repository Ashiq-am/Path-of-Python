# Python3 code to demonstrate
# Maximum element in Cropped List
# using list slicing + max()

# initializing list
test_list = [2, 3, 5, 7, 9, 10, 8, 6]

# printing original list
print ("The original list is : " + str(test_list))

i, j = 2, 5

# Maximum element in Cropped List
# using list slicing + max()
res = test_list[i : j]
res = max(res)

# printing result
print ("The maximum element in range is : " + str(res))
