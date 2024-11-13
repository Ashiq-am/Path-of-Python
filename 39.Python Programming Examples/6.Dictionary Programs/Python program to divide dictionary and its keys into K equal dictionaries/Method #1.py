# Python3 code to demonstrate working of
# Divide dictionary into K equal dictionaries
# Using loop

# initializing dictionary
test_dict = {"Gfg": 20, "is": 36, "best": 100}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing size
K = 4

# contructing new dict
temp = dict()
for key in test_dict:
	temp[key] = test_dict[key] / 4

# creating list
res = []
for idx in range(K):
	res.append(temp)

# printing result
print("Required dictionary list : " + str(res))
