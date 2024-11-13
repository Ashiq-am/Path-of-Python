# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of List
# Using list comprehension

# initializing Dictionary
test_dict = {'gfg' : [1, 3, 4], 'is' : [7, 6], 'best' : [4, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Key-Value list Dictionary to Lists of List
# Using list comprehension
res = [[key] + val for key, val in test_dict.items()]

# printing result
print("The converted list is : " + str(res))
