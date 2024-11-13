# Python3 code to demonstrate
# Records element list Maximum
# using list comprehension + max()

# initializing list
test_list = [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + max()
# Records element list Maximum
res = [(key, max(lst)) for key, lst in test_list]

# print result
print("The list tuple attribute maximum is : " + str(res))
