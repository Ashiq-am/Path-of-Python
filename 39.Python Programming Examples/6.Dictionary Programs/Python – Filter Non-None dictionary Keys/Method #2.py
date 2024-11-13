# Python3 code to demonstrate working of
# Non-None dictionary Keys
# Using dictionary comprehension

# initializing dictionary
test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : None}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Non-None dictionary Keys
# Using dictionary comprehension
res = list({ele for ele in test_dict if test_dict[ele]})

# printing result
print("Non-None keys list : " + str(res))
