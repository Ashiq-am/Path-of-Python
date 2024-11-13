# Python3 code to demonstrate working of
# Boolean composition mask in list
# Using set() + list comprehension

# initializing list
test_list = [5, 2, 1, 9, 8, 0, 4]

# printing original list
print("The original list is : " + str(test_list))

# initializing search list
search_list = [1, 10, 8, 3, 9]

# list comprehension iteration and in operator
# checking composition
# set() removes duplicates
res = [1 if ele in set(search_list) else 0 for ele in test_list]

# printing result
print("The Boolean Masked list : " + str(res))
