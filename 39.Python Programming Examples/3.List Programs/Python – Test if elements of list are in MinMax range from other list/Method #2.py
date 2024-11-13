# Python3 code to demonstrate working of
# Min/Max range test from other list
# Using all() + min() + max()

# initializing list
test_list = [5, 6, 3, 7, 8, 10, 9]

# printing original lists
print("The original list is : " + str(test_list))

# initializing range_list
range_list = [4, 7, 9, 6]

# checking for all values in range using all()
res = all(ele >= min(test_list) and ele <= max(test_list)
		for ele in range_list)

# printing result
print("Are all elements in min/max range? : " + str(res))
