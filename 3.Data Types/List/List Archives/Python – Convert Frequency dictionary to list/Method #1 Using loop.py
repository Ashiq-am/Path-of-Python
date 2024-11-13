# Python3 code to demonstrate working of
# Convert Frequency dictionary to list
# Using loop

# initializing dictionary
test_dict = {'gfg': 4, 'is': 2, 'best': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Convert Frequency dictionary to list
# Using loop
res = []
for key in test_dict:
    for idx in range(test_dict[key]):
        res.append(key)

    # printing result
print("The resultant list : " + str(res))
