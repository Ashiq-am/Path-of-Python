# Python3 code to demonstrate working of
# Change value if value equals K in dictionary
# Using loop

# initializing dictionary
test_dict = {"Gfg": 4, "is": 8, "best": 10, "for": 8, "geeks": 19}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 8

# initializing repl_val
repl_val = 20

# iterating dictionary
for key, val in test_dict.items():

    # checking for required value
    if val == K:
        test_dict[key] = repl_val

# printing result
print("The dictionary after values replacement : " + str(test_dict))
