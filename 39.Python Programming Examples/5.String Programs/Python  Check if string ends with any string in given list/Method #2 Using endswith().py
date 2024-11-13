# Python3 code to demonstrate
# Checking for string match suffix
# using endswith()

# initializing string
test_string = "GfG is best"

# initializing suffix list
suff_list = ['best', 'iss', 'good']

# printing original string
print("The original string : " + str(test_string))

# using endswith()
# Checking for string match suffix
res = test_string.endswith(tuple(suff_list))

# print result
print("Does string end with any suffix list sublist ? : " + str(res))
