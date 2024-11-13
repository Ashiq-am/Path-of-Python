# Python3 code to demonstrate working of
# Change value if value equals K in dictionary
# Using dictionary comprehension

# initializing dictionary
test_dict = {"Gfg": 4, "is": 8, "best": 10, "for": 8, "geeks": 19}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 8

# initializing repl_val
repl_val = 20

# one-liner to solve for dictionary
res = {key : repl_val if val == K else val for key, val in test_dict.items()}

# printing result
print("The dictionary after values replacement : " + str(res))
