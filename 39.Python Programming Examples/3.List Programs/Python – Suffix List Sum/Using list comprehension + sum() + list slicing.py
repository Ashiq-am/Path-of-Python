# Python3 code to demonstrate
# Suffix List Sum
# using list comprehension + sum() + list slicing

# initializing list
test_list = [3, 4, 1, 7, 9, 1]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + sum() + list slicing
# Suffix List Sum
test_list.reverse()
res = [sum(test_list[ : i + 1 ]) for i in range(len(test_list))]

# print result
print("The suffix sum list is : " + str(res))
