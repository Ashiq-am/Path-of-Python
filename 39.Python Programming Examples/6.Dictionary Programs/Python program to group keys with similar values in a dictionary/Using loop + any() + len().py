# Python3 code to demonstrate working of
# Group keys with similar values in Dictionary
# Using loop + any() + len()

# initializing dictionary
test_dict = {"Gfg": [5, 6], "is": [8, 6, 9],
             "best": [10, 9], "for": [5, 2],
             "geeks": [19]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

res = []
for key in test_dict:
    chr = [key]
    for ele in test_dict:

        # check with other keys
        if key != ele:

            # checking for any match in values
            if any(i == j for i in test_dict[key] for j in test_dict[ele]):
                chr.append(ele)
    if len(chr) > 1:
        res.append(chr)

# printing result
print("The dictionary after values replacement : " + str(res))
