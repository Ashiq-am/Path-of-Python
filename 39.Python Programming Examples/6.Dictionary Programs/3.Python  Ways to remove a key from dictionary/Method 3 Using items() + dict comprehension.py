# Python code to demonstrate
# removal of dict. pair
# using items() + dict comprehension

# Initializing dictionary
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}

# Printing dictionary before removal
print ("The dictionary before performing remove is : " + str(test_dict))

# Using items() + dict comprehension to remove a dict. pair
# removes Mani
new_dict = {key:val for key, val in test_dict.items() if key != 'Mani'}

# Printing dictionary after removal
print ("The dictionary after remove is : " + str(new_dict))
