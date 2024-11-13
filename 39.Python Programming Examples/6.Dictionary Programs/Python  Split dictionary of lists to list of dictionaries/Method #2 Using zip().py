# Python3 code to demonstrate
# to convert dictionary of list to
# list of dictionaries
# using zip()

# initializing dictionary
test_dict = { "Rash" : [1, 3], "Manjeet" : [1, 4], "Akash" : [3, 4] }

# printing original dictionary
print ("The original dictionary is : " + str(test_dict))

# using zip()
# to convert dictionary of list to
# list of dictionaries
res = [dict(zip(test_dict, i)) for i in zip(*test_dict.values())]

# printing result
print ("The converted list of dictionaries " + str(res))
