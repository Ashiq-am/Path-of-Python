# Python3 code to demonstrate working of
# Extract ith Key's Value of K's Maximum value dictionary
# Using max() + external function

# custom function as comparator
def cust_fnc(ele):
    return ele.get(K, 0)


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
res = max(test_list, key=cust_fnc)[i]

# printing result
print("The required value : " + str(res))
