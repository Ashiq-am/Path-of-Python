# Python3 code to demonstrate
# Shift zeroes at end of list
# using list comprehension + isinstance()

# initializing list
test_list = [1, 4, None, "Manjeet", False, 0, False, 0, "Nikhil"]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + isinstance()
# Shift zeroes at end of list
temp = [ele for ele in test_list if ele or
		ele is None or isinstance(ele, bool)]
res = temp + [0] * (len(test_list) - len(temp))

# print result
print("The list after shifting 0's to end : " + str(res))
