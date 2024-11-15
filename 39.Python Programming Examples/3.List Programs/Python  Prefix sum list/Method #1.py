# Python3 code to demonstrate
# prefix sum list
# using list comprehension + sum() + list slicing

# initializing list
test_list = [3, 4, 1, 7, 9, 1]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + sum() + list slicing
# prefix sum list
res = [sum(test_list[ : i + 1]) for i in range(len(test_list))]

# print result
print("The prefix sum list is : " + str(res))
