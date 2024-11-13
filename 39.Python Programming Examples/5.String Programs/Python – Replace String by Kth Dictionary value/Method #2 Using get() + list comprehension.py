# Python3 code to demonstrate working of
# Replace String by Kth Dictionary value
# Using get() + list comprehension

# initializing list
test_list = ["Gfg", "is", "Best"]

# printing original list
print("The original list : " + str(test_list))

# initializing subs. Dictionary
subs_dict = {
    "Gfg": [5, 6, 7],
    "is": [7, 4, 2],
}

# initializing K
K = 2

# using list comprehension to solve problem using one liner
# get() to perform presence checks and assign default value
res = [subs_dict.get(ele, ele) for ele in test_list]
res = [ele[K] if isinstance(ele, list) else ele for ele in res]

# printing result
print("The list after substitution : " + str(res))
