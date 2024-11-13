# Python3 code to demonstrate working of
# Search in Nth Column of Matrix
# Using any() + list comprehension

# initializing list
test_list = [[1, 4, 5], [6, 7, 8], [8, 3, 0]]

# printing list
print("The original list : " + str(test_list))

# initializing N
N = 1

# initializing num
ele = 3

# Search in Nth Column of Matrix
# Using any() + list comprehension
res = any(sub[N] == ele for sub in test_list)

# Printing result
print("Does element exists in particular column : " + str(res))
