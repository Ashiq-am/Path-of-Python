# Python3 code to demonstrate working of
# K consecutive Maximum
# Using list comprehension

# initializing list
test_list = [4, 3, 8, 2, 6, 7, 4, 3, 2, 4, 5]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# one-liner to solve problem
res = [max(test_list[idx : idx + K]) for idx in range(len(test_list) - K + 1)]

# printing result
print("Next K Maximum List : " + str(res))
