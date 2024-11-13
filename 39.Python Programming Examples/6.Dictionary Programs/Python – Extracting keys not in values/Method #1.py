# Python3 code to demonstrate working of
# Extracting keys not in values
# Using set() + keys() + values() + loop

# initializing Dictionary
test_dict = {3 : [1, 3, 4], 5 : [1, 2], 6 : [4, 3], 4 : [1, 3]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extracting keys not in values
# Using set() + keys() + values() + loop
temp1 = set(test_dict.keys())
temp2 = set()
for ele in test_dict.values():
	temp2.update(ele)
res = list(temp1 - temp2)

# printing result
print("The extracted keys are : " + str(res))
