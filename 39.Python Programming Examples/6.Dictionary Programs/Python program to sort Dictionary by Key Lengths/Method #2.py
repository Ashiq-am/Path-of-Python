# Python3 code to demonstrate working of
# Sort Dictionary by Key Lengths
# Using sorted() + lambda function + items() + dictionary comprehension

# initializing dictionary
test_dict = {"Gfg" : 4, "is" : 1, "best" : 0, "for" : 3, "geeks" : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# sorting using sorted()
# lambda fnc. to render logic
test_dict_list = sorted(list(test_dict.items()), key = lambda key : len(key[0]))

# reordering to dictionary
res = {ele[0] : ele[1] for ele in test_dict_list}

# printing result
print("The sorted dictionary : " + str(res))
