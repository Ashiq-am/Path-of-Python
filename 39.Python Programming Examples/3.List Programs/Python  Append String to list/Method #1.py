# Python3 code to demonstrate working of
# Appending String to list
# using + operator + list conversion

# initialize list
test_list = [1, 3, 4, 5]

# initialize string
test_str = 'gfg'

# printing original list
print("The original list : " + str(test_list))

# printing original string
print("The original string : " + str(test_str))

# Appending String to list
# using + operator + list conversion
test_list += [test_str]

# printing result
print("The list after appending is : " + str(test_list))
