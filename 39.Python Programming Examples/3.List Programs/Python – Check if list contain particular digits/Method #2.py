# Python3 code to demonstrate working of
# Test if list contain particular digits
# Using any() + list comprehension

# initializing lists
test_list = [435, 133, 113, 451, 134]

# printing original list
print("The original list is : " + str(test_list))

# initializing digits
digs = [1, 4, 5, 3]

digt_str = ''.join([str(ele) for ele in digs])
all_ele = ''.join([str(ele) for ele in test_list])

# any() checks if any element is not part of digit
res = not any(ele not in digt_str for ele in all_ele)

# printing result
print("Are all elements made from required digits? : " + str(res))
