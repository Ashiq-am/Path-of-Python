# Python3 code to demonstrate working of
# Convert Strings to Uppercase in Dictionary value lists
# Using dictionary comprehension + upper() + list comprehension

# initializing dictionary
test_dict = {"Gfg" : ["ab", "cd", "ef"],
			"Best" : ["gh", "ij"], "is" : ["kl"]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using upper to convert to upper case
res = {key: [ele.upper() for ele in test_dict[key] ] for key in test_dict }

# printing result
print("The dictionary after conversion " + str(res))
