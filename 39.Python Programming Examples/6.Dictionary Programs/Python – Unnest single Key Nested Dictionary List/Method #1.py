# Python3 code to demonstrate working of
# Unnest single Key Nested Dictionary List
# Using loop + items()

# initializing list
test_list = [{'gfg' : {'data' : 1}}, {'is' : {'data' : 5}}, {'best' : {'data' : 4}}]

# printing original list
print("The original list is : " + str(test_list))

# initializing key
data_key = 'data'

# Unnest single Key Nested Dictionary List
# Using loop + items()
res = dict()
for sub in test_list:
	for key, val in sub.items():
		res[key] = sub[key][data_key]

# printing result
print("The constructed Dictionary list : " + str(res))
