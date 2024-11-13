# Python3 code to demonstrate working of
# Remove Negative Elements in List
# Using list comprehension

# initializing list
test_list = [5, 6, -3, -8, 9, 11, -12, 2]

# printing original list
print("The original list is : " + str(test_list))

# Remove Negative Elements in List
# Using list comprehension
res = [ele for ele in test_list if ele > 0]

# printing result
print("List after filtering : " + str(res))
