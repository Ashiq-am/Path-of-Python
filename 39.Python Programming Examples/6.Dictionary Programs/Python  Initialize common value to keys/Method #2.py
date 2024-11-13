# Python3 code to demonstrate working of
# Initialize common value to keys
# Using get() + default value

# Initialize dictionary
test_dict = dict()

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Initialize common value to keys
# Using get() + default value
res_demo = test_dict.get('Geeks', 4)

# printing result
print("The value of key is : " + str(res_demo))
