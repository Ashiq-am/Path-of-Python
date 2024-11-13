# Python3 code to demonstrate working of
# Append Missing elements from other List
# Using set() + "-" operator + extend()

# initializing list
test_list1 = [5, 6, 4, 8, 9, 1]
test_list2 = [9, 8, 7]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# finding missing words
rem_list = (set(test_list1) - set(test_list2))

# checking order
res = [ele for ele in test_list1 if ele in rem_list]

# joining result
res.extend(test_list2)

# printing result
print("The modified list 2 : " + str(res))
