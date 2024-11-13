# Python3 code to demonstrate working of
# Positions of maximum element in list
# Using list comprehension + max() + enumerate()

# initializing list
test_list = [8, 4, 6, 8, 2, 8]

# printing list
print("The original list : " + str(test_list))

# Positions of maximum element in list
# Using list comprehension + max() + enumerate()
temp = max(test_list)
res = [i for i, j in enumerate(test_list) if j == temp]

# Printing result
print("The Positions of maximum element : " + str(res))
