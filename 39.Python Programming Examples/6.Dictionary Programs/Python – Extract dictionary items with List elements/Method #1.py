# Python3 code to demonstrate working of
# Extract dictionary items with List elements
# Using set() + dictionary comprehension + items()

# helpr_fnc
def hlper_fnc(req_list, test_dict):
    temp = set(req_list)
    temp2 = {key: set(val) for key, val in test_dict.items()}
    return {key: val for key, val in test_dict.items() if temp2[key].issubset(temp)}


# initializing dictionary
test_dict = {'gfg': [4, 6], 'is': [10], 'best': [4, 5, 7]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing req_list
req_list = [4, 6, 10]

# Extract dictionary items with List elements
# Using set() + dictionary comprehension + items()
res = hlper_fnc(req_list, test_dict)

# printing result
print("The extracted dictionary: " + str(res))
