# Python3 code to demonstrate working of
# Divide dictionary into K equal dictionaries
# Using dictionary comprehension + list comprehension


# function to divide dictionary
# and keys into K equal dictionaries
def divideDictKeys(dictionary, K):

	# contructing new dict
	# using dictionary comprehension
	temp = {key: test_dict[key] / K for key in test_dict}

	# creating list
	# using list comprehension
	res = [temp for idx in range(K)]

	return str(res)


# driver code

# initializing dictionary
test_dict = {"Gfg": 20, "is": 36, "best": 100}

# initializing size
K = 4

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# printing result
print("Required dictionary list : " + divideDictKeys(test_dict, K))
