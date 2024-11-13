# Python3 code to demonstrate working of
# Remove N from K key's value in dictionary values list
# Using loop + conditional statements

# initializing dictionary
test_dict = {"gfg": [9, 4, 5, 2, 3, 2],
             "is": [1, 2, 3, 4, 3, 2],
             "best": [2, 2, 2, 3, 4]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K, N
K, N = "gfg", 2

res = dict()
for key, val in test_dict.items():
    # reassigning omitting desired number
    res[key] = (val if key != K else [idx for idx in val if idx != N])

# printing result
print("The altered dictionary : " + str(res))
