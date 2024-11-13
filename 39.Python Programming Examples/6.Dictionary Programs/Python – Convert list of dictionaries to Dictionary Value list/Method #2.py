# Python3 code to demonstrate working of
# Convert list of dictionaries to Dictionary Value list
# Using list comprehension + dictionary comprehension
from collections import defaultdict

# initializing lists
test_list = [{"Gfg": 6, "is": 9, "best": 10},
             {"Gfg": 8, "is": 11, "best": 19},
             {"Gfg": 2, "is": 16, "best": 10},
             {"Gfg": 12, "is": 1, "best": 8},
             {"Gfg": 22, "is": 6, "best": 8}]

# printing original list
print("The original list : " + str(test_list))

# dictionary and list comprehension
# for shorthand to solution of problem
res = defaultdict(list)
{res[key].append(sub[key]) for sub in test_list for key in sub}

# printing result
print("The extracted dictionary : " + str(dict(res)))
