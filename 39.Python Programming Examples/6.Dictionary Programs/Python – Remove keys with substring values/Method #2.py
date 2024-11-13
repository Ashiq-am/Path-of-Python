# Python3 code to demonstrate working of
# Remove keys with substring values
# Using dictionary comprehension + any()

# initializing dictionary
test_dict = {1: 'Gfg is best for geeks', 2: 'Gfg is good', 3: 'I love Gfg'}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing substrings
sub_list = ['love', 'good']

# Remove keys with substring values
# Using dictionary comprehension + any()
res = {key: val for key, val in test_dict.items() if not any(ele in val for ele in sub_list)}

# printing result
print("Filtered Dictionary : " + str(res))
