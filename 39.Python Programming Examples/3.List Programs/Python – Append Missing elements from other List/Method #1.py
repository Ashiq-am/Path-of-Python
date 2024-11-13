# Python3 code to demonstrate working of
# Append Missing elements from other List
# Using list comprehension

# initializing list
test_list1 = [5, 6, 4, 8, 9, 1]
test_list2 = [9, 8, 7]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# extracting elements from list 1 which are not in list 2
temp1 = [ele for ele in test_list1 if ele not in test_list2]

# constructing result
res = temp1 + test_list2

# printing result
print("The modified list 2 : " + str(res))
