# Python3 code to demonstrate working of
# Remove Negative Elements in List
# Using filter() + lambda

# initializing list
test_list = [5, 6, -3, -8, 9, 11, -12, 2]

# printing original list
print("The original list is : " + str(test_list))

# Remove Negative Elements in List
# Using filter() + lambda
res = list(filter(lambda x : x > 0, test_list))

# printing result
print("List after filtering : " + str(res))
