# Python3 code to demonstrate working of
# Flatten Dictionary with List
# Using chain.from_iterable() + list comprehension
from itertools import chain

# initializing list
test_list = ["Gfg", "is", "Best", "For", "Geeks"]

# printing original list
print("The original list : " + str(test_list))

# initializing subs. Dictionary
subs_dict = {"Gfg": 7, "Geeks": 8}

temp = ([ele, subs_dict[ele]] if ele in subs_dict
        else [ele] for ele in test_list)

# chain.from_iterable() for flattening
res = list(chain.from_iterable(temp))

# printing result
print("The list after substitution : " + str(res))
