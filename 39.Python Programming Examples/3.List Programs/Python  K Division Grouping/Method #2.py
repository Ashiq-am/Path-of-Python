# Python3 code to demonstrate
# K Division Grouping
# using list comprehension + min() + max()

# initializing list
test_list = [3, 12, 13, 22, 25, 30]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 7

# using list comprehension + min() + max()
# K Division Grouping
temp = sorted(test_list)
res = [[ele for ele in temp if ele // K == sub] for sub in range(min(test_list) // K, (max(test_list) // K) + 1)]

# print result
print("The list after grouping by K is : " + str(res))
