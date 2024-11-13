# Python3 code to demonstrate working of
# Values derived Dictionary keys
# Using loop

# initializing list
test_list = ["gfg", "is", "best"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = "def_key_"

# using loop to construct new Dictionary
# + operator used to concat default key and values
res = dict()
for ele in test_list:
	res[K + str(ele)] = ele

# printing result
print("The constructed Dictionary : " + str(res))
