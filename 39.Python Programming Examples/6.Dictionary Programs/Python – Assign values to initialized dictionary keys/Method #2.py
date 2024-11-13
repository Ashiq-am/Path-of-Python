# Python3 code to demonstrate working of
# Assign values to initialized dictionary keys
# using loop + zip()

# initializing dictionary
test_dict = {'gfg': '', 'is': '', 'best': ''}

# Initializing list
test_list = ['A', 'B', 'C']

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Assign values to initialized dictionary keys
# using loop + zip()
for key, val in zip(test_dict, test_list):
    test_dict[key] = val

# printing result
print("The assigned value dictionary is : " + str(test_dict))
