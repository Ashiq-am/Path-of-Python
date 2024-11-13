# Python3 code to demonstrate working of
# Extract ith Key's Value of K's Maximum value dictionary
# Using max() + lambda

# initializing lists
test_list = [{"Gfg": 3, "is": 9, "best": 10},
             {"Gfg": 8, "is": 11, "best": 19},
             {"Gfg": 9, "is": 16, "best": 1}]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = "best"

# initializing i
i = "Gfg"

# using get() to handle missing key, assigning lowest value
res = max(test_list, key=lambda ele: ele.get(K, 0))[i]

# printing result
print("The required value : " + str(res))
