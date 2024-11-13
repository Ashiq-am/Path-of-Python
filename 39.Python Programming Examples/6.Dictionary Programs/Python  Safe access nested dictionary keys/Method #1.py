# Python3 code to demonstrate working of
# Safe access nested dictionary key
# Using nested get()

# initializing dictionary
test_dict = {'Gfg' : {'is' : 'best'}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using nested get()
# Safe access nested dictionary key
res = test_dict.get('Gfg', {}).get('is')

# printing result
print("The nested safely accessed value is : " + str(res))
