# Python3 code to demonstrate working of
# Value's Key association
# Using list comprehension + any()

# initializing dictionary
test_dict = {'gfg' : [4, 5], 'is' : [8], 'best' : [10, 12]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing value list
val_list = [5, 10]

# Value's Key association
# Using list comprehension + any()
res = [key for key, val in test_dict.items() if any(y in val for y in val_list)]

# printing result
print("The keys mapped to " + str(val_list) + " are : " + str(res))
