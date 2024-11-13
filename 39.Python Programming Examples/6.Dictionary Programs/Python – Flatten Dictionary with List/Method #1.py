# Python3 code to demonstrate working of
# Flatten Dictionary with List
# Using get() + list comprehension

# initializing list
test_list = ["Gfg", "is", "Best", "For", "Geeks"]

# printing original list
print("The original list : " + str(test_list))

# initializing subs. Dictionary
subs_dict = {"Gfg": 7, "Geeks": 8}

# get() to perform presence checks and assign value
temp = object()
res = [ele for sub in ((ele, subs_dict.get(ele, temp))
                       for ele in test_list) for ele in sub if ele != temp]

# printing result
print("The list after substitution : " + str(res))
