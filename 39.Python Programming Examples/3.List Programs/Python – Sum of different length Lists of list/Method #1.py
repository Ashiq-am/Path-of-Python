# Python3 code to demonstrate
# Sum of Uneven Lists of list
# Using list comprehension + sum()

# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + sum()
# Sum of Uneven Lists of list
res = sum([ele for sub in test_list for ele in sub])

# print result
print("The total element sum in lists is : " + str(res))
