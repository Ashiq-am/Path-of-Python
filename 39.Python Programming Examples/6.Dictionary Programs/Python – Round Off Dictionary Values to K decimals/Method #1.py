# Python3 code to demonstrate working of
# Round Off Dictionary Values to K decimals
# Using loop + round()

# initializing dictionary
test_dict = {"Gfg": 54.684034, "is": 76.324334, "Best": 28.43524}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 3

# loop to iterate for values
res = dict()
for key in test_dict:
    # rounding to K using round()
    res[key] = round(test_dict[key], K)

# printing result
print("Values after round off : " + str(res))
