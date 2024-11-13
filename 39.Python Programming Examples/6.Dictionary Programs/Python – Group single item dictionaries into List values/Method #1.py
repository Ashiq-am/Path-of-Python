# Python3 code to demonstrate working of
# Group single item dictionaries into List values
# Using setdefault() + loop

# initializing lists
test_list = [{"Gfg": 3}, {"is": 8}, {"Best": 10}, {"Gfg": 18}, {"Best": 33}]

# printing original list
print("The original list : " + str(test_list))

res = {}

# using loop to loop through each dictionary
for idx in test_list:

    # items() to extract item
    for key, val in idx.items():
        # setdefault performs task of setting empty list value as default
        res.setdefault(key, []).append(val)

# printing result
print("The constructed dictionary : " + str(res))
