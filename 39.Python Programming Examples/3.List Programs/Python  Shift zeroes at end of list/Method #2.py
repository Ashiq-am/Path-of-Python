# Python3 code to demonstrate
# Shift zeroes at end of list
# using list comprehension + isinstance() + list slicing

# initializing list
test_list = [1, 4, None, "Manjeet", False, 0, False, 0, "Nikhil"]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + isinstance() + list slicing
# Shift zeroes at end of list
res = ([ele for ele in test_list if not isinstance(ele, int)
		or ele or isinstance(ele, bool)]
		+ [0] * len(test_list))[:len(test_list)]

# print result
print("The list after shifting 0's to end : " + str(res))
