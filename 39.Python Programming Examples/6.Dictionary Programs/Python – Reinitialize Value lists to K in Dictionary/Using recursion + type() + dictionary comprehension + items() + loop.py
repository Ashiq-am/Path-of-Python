# Python3 code to demonstrate working of
# Reinitialize Value lists to K in Dictionary
# Using recursion + type() + dictionary comprehension + items() + loop

# helpr function
def helpr_fnc(ele, K):
    if type(ele) is list:
        return [helpr_fnc(val, K) for val in ele]
    elif type(ele) is dict:
        return {key: helpr_fnc(val, K) for key, val in ele.items()}
    return K


# initializing dictionary
test_dict = {'gfg': [4, 6, 7], 'is': 8, 'best': [[4, 5], [8, 9, 20]]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing K
K = 4

# Reinitialize Value lists to K in Dictionary
# Using recursion + type() + dictionary comprehension + items() + loop
res = helpr_fnc(test_dict, K)

# printing result
print("The Reinitialized dictionary : " + str(dict(res)))
