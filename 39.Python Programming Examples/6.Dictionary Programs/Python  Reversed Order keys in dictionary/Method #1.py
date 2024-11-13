# Python3 code to demonstrate working of
# Reversed Order keys in dictionary
# Using sorted() + keys() + reversed() + loop

# initializing dictionary
test_dict = {1 : "Gfg", 5 : "is", 4 : "the", 2 : "best"}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using sorted() + keys() + reversed() + loop
# Reversed Order keys in dictionary
res = []
for ele in reversed(sorted(test_dict.keys())):
	res.append(ele)

# printing result
print("The reversed order of dictionary keys : " + str(res))
