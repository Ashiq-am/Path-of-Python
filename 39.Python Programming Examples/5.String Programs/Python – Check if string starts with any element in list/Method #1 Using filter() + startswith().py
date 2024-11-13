# Python3 code to demonstrate
# Prefix tests in Strings
# using filter() + startswith()

# initializing string
test_string = "GfG is best"

# initializing prefix list
pref_list = ['best', 'GfG', 'good']

# printing original string
print("The original string : " + str(test_string))

# using filter() + startswith()
# Prefix tests in Strings
res = list(filter(test_string.startswith, pref_list)) != []

# print result
print("Does string start with any prefix list sublist ? : " + str(res))
