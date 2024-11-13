# Python3 code to demonstrate working of
# Minimum element indices
# Using list comprehension + min() + enumerate()

# initializing list
test_list = [2, 4, 6, 8, 2, 2]

# printing list
print("The original list : " + str(test_list))

# Minimum element indices
# Using list comprehension + min() + enumerate()
temp = min(test_list)
res = [i for i, j in enumerate(test_list) if j == temp]

# Printing result
print("The Positions of minimum element : " + str(res))
