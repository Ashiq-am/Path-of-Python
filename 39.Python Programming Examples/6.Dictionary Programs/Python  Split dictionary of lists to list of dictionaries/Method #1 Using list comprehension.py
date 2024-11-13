# Python3 code to demonstrate
# to convert dictionary of list to
# list of dictionaries
# using list comprehension

# initializing dictionary
test_dict = { "Rash" : [1, 3], "Manjeet" : [1, 4], "Akash" : [3, 4] }

# printing original dictionary
print ("The original dictionary is : " + str(test_dict))

# using list comprehension
# to convert dictionary of list to
# list of dictionaries
res = [{key : value[i] for key, value in test_dict.items()}
		for i in range(2)]

# printing result
print ("The converted list of dictionaries " + str(res))
