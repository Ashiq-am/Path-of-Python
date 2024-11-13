# Python3 code to demonstrate working of
# Remove Key from Dictionary List
# Using list comprehnsion + dictionary comprehension

# initializing list
test_list = [{'Gfg' : 1, 'id' : 2, 'best' : 8 },
			{'Gfg' : 4, 'id' : 4, 'best': 10},
			{'Gfg' : 4, 'id' : 8, 'best': 11}]

# printing original list
print("The original list is : " + str(test_list))

# initializing key
del_key = 'id'

# Remove Key from Dictionary List
# Using list comprehnsion + dictionary comprehension
res = [{key : val for key, val in sub.items() if key != del_key} for sub in test_list]

# printing result
print("The modified list : " + str(res))
