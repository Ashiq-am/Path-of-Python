# Python3 code to demonstrate
# Rear shift K in List
# using list comprehension + isinstance()

# initializing list
test_list = [1, 4, None, "Manjeet", False, 4, False, 4, "Nikhil"]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 4

# using list comprehension + isinstance()
# Rear shift K in List
temp = [ele for ele in test_list if ele != K and ele or ele is None or isinstance(ele, bool) ]
res = temp + [K] * (len(test_list) - len(temp))

# print result
print("The list after shifting K's to end : " + str(res))
