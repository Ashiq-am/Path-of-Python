# Python3 code to demonstrate working of
# Functions as dictionary values
# Using Without params

# call Gfg fnc
def print_key1():
	return "This is Gfg's value"

# initializing dictionary
# check for function name as key
test_dict = {"Gfg": print_key1, "is" : 5, "best" : 9}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# calling function using brackets
res = test_dict['Gfg']()

# printing result
print("The required call result : " + str(res))
