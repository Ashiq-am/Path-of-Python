# Python3 code to demonstrate working of
# Unique Dictionary Value List elements
# Using loop

# initializing dictionary
test_dict = {"Gfg": [6, 7, 4, 6],
             "is": [8, 9, 5],
             "for": [2, 5, 3, 7],
             "Geeks": [6, 8, 5, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# list to memorize elements and insert result
res = []
for sub in test_dict:
    for ele in test_dict[sub]:

        # testing for existence
        if ele not in res:
            res.append(ele)

# printing result
print("Extracted items : " + str(res))
