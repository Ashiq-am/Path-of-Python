# Python3 code to demonstrate working of
# Concatenate Tuple to Dictionary Key
# Using dictionary comprehension

# initializing list
test_list = [(("gfg", "is", "best"), 10), (("gfg", "good"), 1), (("gfg", "for", "cs"), 15)]

# printing original list
print("The original list is : " + str(test_list))

# one liner to solve problem
res = {' '.join(key): val for key, val in test_list}

# printing result
print("The computed Dictionary : " + str(res))
