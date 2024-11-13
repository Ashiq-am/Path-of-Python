# Python3 code to demonstrate working of
# Filter Dictionary Key Possible Element rows
# Using filter() + lambda + isinstance() + all()

# initializing list
test_list = [[4, 5, [2, 3, 2]], ["gfg", 1, (4, 4)], [{5: 4}, 3, "good"], [
	True, "best"]]

# printing original list
print("The original list is : " + str(test_list))

# checking for each immutable data type
# filtering using filter()
res = list(filter(lambda row: all(isinstance(ele, int) or isinstance(ele, bool)
								or isinstance(ele, float) or isinstance(ele, tuple)
								or isinstance(ele, str) for ele in row), test_list))

# printing result
print("Filtered rows : " + str(res))
