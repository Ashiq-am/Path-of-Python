# Python3 code to demonstrate working of
# Maximum value from List keys
# Using loop

# initializing dictionary
test_dict = {"Gfg": 4, "is": 5, "best": 9,
             "for": 11, "geeks": 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing list
test_list = ["Gfg", "best", "geeks"]

res = 0
for ele in test_list:

    # checking for key in dictionary
    if ele in test_dict:
        res = max(res, test_dict[ele])

# printing result
print("The required maximum : " + str(res))
