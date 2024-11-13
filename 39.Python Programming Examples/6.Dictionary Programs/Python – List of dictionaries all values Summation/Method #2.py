# Python3 code to demonstrate working of
# List of dictionaries all values Summation
# Using sum() + values() + list comprehension

# initializing lists
test_list = [{"Gfg": 6, "is": 9, "best": 10},
             {"Gfg": 8, "is": 11, "best": 19},
             {"Gfg": 2, "is": 16, "best": 10},
             {"Gfg": 12, "is": 1, "best": 8},
             {"Gfg": 22, "is": 6, "best": 8}]

# printing original list
print("The original list : " + str(test_list))

res = sum([sum(list(sub.values())) for sub in test_list])

# printing result
print("The computed sum : " + str(res))
