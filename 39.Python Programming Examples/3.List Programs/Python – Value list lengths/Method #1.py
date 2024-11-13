# Python3 code to demonstrate
# Value list lengths
# using list comprehension + len()

# initializing list
test_list = [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + len()
# Value list lengths
res = [(key, len(lst)) for key, lst in test_list]

# print result
print("The list tuple attribute length is : " + str(res))
