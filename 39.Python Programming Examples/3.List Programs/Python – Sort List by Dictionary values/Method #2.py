# Python3 code to demonstrate working of
# Sort List by Dictionary values
# Using sorted() + key + get()

# initializing list
test_list = ['gfg', 'is', 'best']

# initializing Dictionary
test_dict = {'gfg' : 56, 'is' : 12, 'best' : 76}

# printing original list
print("The original list is : " + str(test_list))

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Sort List by Dictionary values
# Using sorted() + key + get()
res = sorted(test_list, key = test_dict.get)

# printing result
print("The list after sorting : " + str(res))
