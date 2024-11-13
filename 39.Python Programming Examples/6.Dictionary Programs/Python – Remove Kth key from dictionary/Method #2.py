# Python3 code to demonstrate working of
# Remove Kth key from dictionary
# Using Remove Kth key from dictionary

# initializing dictionary
test_dict = {"Gfg": 20, "is": 36, "best": 100,
             "for": 17, "geeks": 1}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing size
K = 3

# dictionary comprehension remakes dictionary,
# rather than removing
res = {key: val for key, val in test_dict.items()
       if key != list(test_dict.keys())[K - 1]}

# printing result
print("Required dictionary after removal : " + str(res))
