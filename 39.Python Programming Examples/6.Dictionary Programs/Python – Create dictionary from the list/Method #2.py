# Python3 code to demonstrate working of
# Values derived Dictionary keys
# Using dictionary comprehension

# initializing list
test_list = ["gfg", "is", "best"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = "def_key_"

# using dictionary comprehension
# + operator used to concat default key and values
res = {K + str(ele) : ele for ele in test_list}

# printing result
print("The constructed Dictionary : " + str(res))
