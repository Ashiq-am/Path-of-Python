# Python3 code to demonstrate working of
# Synchronized Sorting
# Using dictionary comprehension + sorted() + list comprehension

# initializing dictionary
test_dict = {"Gfg": [4, 6, 7, 3, 10],
             'is': [7, 5, 9, 10, 11],
             'best': [1, 2, 10, 21, 12]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing sort key
sort_key = "Gfg"

# Synchronized Sorting
# Using dictionary comprehension + sorted() + list comprehension
temp = [ele for ele, idx in sorted(enumerate(test_dict[sort_key]),
                                   key=lambda x: x[1])]

res = {key: [val[idx] for idx in temp] for key, val in test_dict.items()}

# printing result
print("The Synchronized sorted dictionary : " + str(res))
