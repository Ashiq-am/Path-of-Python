# initializing dictionary
test_dict = {"Gfg": 3, "is": 5, "for": 8,
             "Geeks": 10, "Best": 16}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing list
sub_list = [5, 4, 10, 20, 16]

# Using loop to perform iteration
res = dict()

for key in test_dict:

    if test_dict[key] in sub_list:
        res[key] = test_dict[key]

# printing result
print("Extracted items : " + str(res))
