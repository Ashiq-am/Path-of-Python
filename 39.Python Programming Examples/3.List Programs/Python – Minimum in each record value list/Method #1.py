# Python3 code to demonstrate
# Record Value list Minimum
# using list comprehension + min()

# initializing list
test_list = [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + min()
# Record Value list Minimum
res = [(key, min(lst)) for key, lst in test_list]

# print result
print("The list tuple attribute minimum is : " + str(res))
