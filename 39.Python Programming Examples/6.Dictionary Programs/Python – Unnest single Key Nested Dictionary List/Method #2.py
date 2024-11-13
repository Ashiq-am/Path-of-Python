# Python3 code to demonstrate working of
# Unnest single Key Nested Dictionary List
# Using list comprehension

# initializing list
test_list = [{'gfg' : {'data' : 1}}, {'is' : {'data' : 5}}, {'best' : {'data' : 4}}]

# printing original list
print("The original list is : " + str(test_list))

# initializing key
data_key = 'data'

# Unnest single Key Nested Dictionary List
# Using list comprehension
res = {x : y[data_key] for idx in test_list for x, y in idx.items()}

# printing result
print("The constructed Dictionary list : " + str(res))
