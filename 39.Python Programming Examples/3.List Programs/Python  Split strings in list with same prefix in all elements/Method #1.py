# Python3 code to demonstrate
# Split strings in list
# Using list comprehension + list slicing

# initializing list
test_list = ['Rs.25', 'Rs.100', 'Rs.143', 'Rs.12', 'Rs.4010']

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + list slicing
# Split strings in list
res = [sub[3:] for sub in test_list]

# print result
print("The list after string slicing : " + str(res))
