# Python3 code to demonstrate working of
# Add prefix to each key name in dictionary
# Using loop

# initializing dictionary
test_dict = {'Gfg' : 6, 'is' : 7, 'best' : 9, 'for' : 8, 'geeks' : 11}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing prefix
temp = "Pro"

# + operator is used to perform task of concatenation
res = {temp + str(key): val for key, val in test_dict.items()}

# printing result
print("The extracted dictionary : " + str(res))
