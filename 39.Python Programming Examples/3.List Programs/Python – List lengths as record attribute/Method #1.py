# Python3 code to demonstrate
# List lengths as record attribute
# using list comprehension + len()

# initializing list
test_list = [('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + len()
# List lengths as record attribute
res = [(key, len(lst)) for key, lst in test_list]

# print result
print("The list tuple attribute lengths is : " + str(res))
