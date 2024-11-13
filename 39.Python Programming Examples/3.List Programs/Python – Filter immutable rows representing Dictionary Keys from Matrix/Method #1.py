# Python3 code to demonstrate working of
# Filter Dictionary Key Possible Element rows
# Using all() + isinstance()

# initializing list
test_list = [[4, 5, [2, 3, 2]], ["gfg", 1, (4, 4)], [{5: 4}, 3, "good"], [
	True, "best"]]

# printing original list
print("The original list is : " + str(test_list))

# checking for each immutable data type
res = [row for row in test_list if all(isinstance(ele, int) or isinstance(ele, bool)
									or isinstance(ele, float) or isinstance(ele, tuple)
									or isinstance(ele, str) for ele in row)]

# printing result
print("Filtered rows : " + str(res))
