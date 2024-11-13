# Python3 code to demonstrate working of
# Convert Strings to Uppercase in Dictionary value lists
# Using map() + upper() + dictionary comprehension

# initializing dictionary
test_dict = {"Gfg" : ["ab", "cd", "ef"],
			"Best" : ["gh", "ij"], "is" : ["kl"]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using map() to extend logic to all inner list
res = {key: list(map(str.upper, test_dict[key])) for key in test_dict}

# printing result
print("The dictionary after conversion " + str(res))
