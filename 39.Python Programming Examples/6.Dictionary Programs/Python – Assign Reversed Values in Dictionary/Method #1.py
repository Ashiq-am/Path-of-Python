# Python3 code to demonstrate working of
# Assign Reversed Values in Dictionary
# Using reversed() + loop + values()

# initializing dictionary
test_dict = {1 : "Gfg", 2 : "is", 3 : "Best"}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# extract values using values()
new_val = list(reversed(list(test_dict.values())))

# reassign new values
res = dict()
cnt = 0
for key in test_dict:
	res[key] = new_val[cnt]
	cnt += 1

# printing result
print("Reassigned reverse values : " + str(res))
