# Python3 code to demonstrate working of
# Filter index similar values
# Using list comprehension + dictionary comprehension

# initializing dictionary
test_dict = {"Gfg": [1, 4, 5, 6, 7], "is": [5, 6, 8, 9, 10],
             "best": [10, 7, 4, 11, 23]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing value list
filt_list = [4, 5, 7]

# Filter index similar values
# Using list comprehension + dictionary comprehension
temp = [test_dict['Gfg'].index(idx) for idx in filt_list]
res = {key: [test_dict[key][idx] for idx in temp] for key in test_dict.keys()}

# printing result
print("The filtered dictionary : " + str(res))
