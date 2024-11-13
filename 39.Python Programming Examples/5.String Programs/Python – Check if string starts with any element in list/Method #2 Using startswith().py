# Python3 code to demonstrate
# Prefix tests in Strings
# using startswith()

# initializing string
test_string = "GfG is best"

# initializing prefix list
pref_list = ['best', 'GfG', 'good']

# printing original string
print("The original string : " + str(test_string))

# using startswith()
# Prefix tests in Strings
res = test_string.startswith(tuple(pref_list))

# print result
print("Does string start with any prefix list sublist ? : " + str(res))
