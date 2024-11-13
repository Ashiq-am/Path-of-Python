# Python3 code to demonstrate working of
# Remove multiple keys from dictionary
# Using pop() + list comprehension

# initializing dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'CS' : 5}

# initializing Remove keys
rem_list = ['is', 'for', 'CS']

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using pop() + list comprehension
# Remove multiple keys from dictionary
[test_dict.pop(key) for key in rem_list]

# printing result
print("Dictionary after removal of keys : " + str(test_dict))
