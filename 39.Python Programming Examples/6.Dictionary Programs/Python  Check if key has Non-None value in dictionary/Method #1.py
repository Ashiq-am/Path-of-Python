# Python3 code to demonstrate working of
# Check if key has Non-None value in dictionary
# Using if

# Initialize dictionary
test_dict = {'gfg': None, 'is': 4, 'for': 2, 'CS': 10}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using if
# Check if key has Non-None value in dictionary
res = False
if test_dict['gfg']:
    res = True

# printing result
print("Does gfg have a Non-None value? : " + str(res))
