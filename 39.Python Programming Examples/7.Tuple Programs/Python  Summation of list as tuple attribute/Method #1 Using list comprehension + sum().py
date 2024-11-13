# Python3 code to demonstrate
# Summation of list as tuple attribute
# using list comprehension + sum()

# initializing list
test_list = [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + sum()
# Summation of list as tuple attribute
res = [(key, sum(lst)) for key, lst in test_list]

# print result
print("The list tuple attribute summation is : " + str(res))
