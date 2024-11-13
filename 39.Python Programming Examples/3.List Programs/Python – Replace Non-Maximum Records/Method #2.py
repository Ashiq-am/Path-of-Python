# Python3 code to demonstrate working of
# Replace Non-Maximum Records
# Using list comprehension + map() + filter() + lambda

# initializing list
test_list = [(1, 4), (9, 11), (4, 6), (6, 8), (9, 11)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = None

# Replace Non-Maximum Records
# Using list comprehension + map() + filter() + lambda
temp = list(filter(lambda ele: ele == max(test_list), test_list))
res = [ele if ele in temp else K for ele in test_list]

# printing result
print("The list after replacing Non-Maximum : " + str(res))
