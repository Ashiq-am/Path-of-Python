# Python3 code to demonstrate working of
# Fill gaps in consecutive Records
# Using min() + max() + dict() + list comprehension

# initializing list
test_list = [(1, 4), (3, 5), (4, 6), (7, 8), (9, 11)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K value
K = "New"

# Fill gaps in consecutive Records
# Using min() + max() + dict() + list comprehension
test_list = dict(test_list)
mini, maxi = min(test_list), max(test_list)
res = [(idx, test_list.get(idx)) for idx in range(mini, maxi + 1)]

# printing result
print("The list after filling gaps : " + str(res))
