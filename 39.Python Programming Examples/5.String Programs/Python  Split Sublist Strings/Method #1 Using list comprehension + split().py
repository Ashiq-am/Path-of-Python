# Python3 code to demonstrate
# Split Sublist Strings
# using split() + list comprehension

# initializing list
test_list = [['GfG is best'], ['All love Gfg'], ['Including me']]

# printing original list
print("The original list : " + str(test_list))

# using split() + list comprehension
# Split Sublist Strings
res = [sub.split() for subl in test_list for sub in subl]

# print result
print("The list after splitting strings : " + str(res))
