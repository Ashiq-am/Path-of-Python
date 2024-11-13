# Python3 code to demonstrate working of
# Rearrange dictionary for consective value-keys
# Using loop + keys()

# initializing dictionary
test_dict = {1 : 3, 4 : 5, 3 : 4, 5 : 6}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Rearrange dictionary for consective value-keys
# Using loop + keys()
temp = list(test_dict.keys())[0]
res = {}
while len(test_dict) > len(res):
	res[temp] = temp = test_dict[temp]

# printing result
print("The rearranged dictionary : " + str(res))
