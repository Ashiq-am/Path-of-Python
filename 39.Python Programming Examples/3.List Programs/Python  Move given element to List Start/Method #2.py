# Python3 code to demonstrate
# Move all K element to List Start
# using list comprehension + isinstance() + list slicing

# initializing list
test_list = [1, 4, None, "Manjeet", False, 4, False, 4, "Nikhil"]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 4

# using list comprehension + isinstance() + list slicing
# Move all K element to List Start
res = ([K] * len(test_list) + [ele for ele in test_list if ele != K and ele or not isinstance(ele, int)
	or isinstance(ele, bool)])[len([ele for ele in test_list if ele != K and ele or not isinstance(ele, int)
	or isinstance(ele, bool)]):]

# print result
print("The list after shifting K's to end : " + str(res))
