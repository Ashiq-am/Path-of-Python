# Python3 code to demonstrate working of
# Remove Key from Dictionary List
# Using loop + del

# initializing list
test_list = [{'Gfg' : 1, 'id' : 2, 'best' : 8 },
			{'Gfg' : 4, 'id' : 4, 'best': 10},
			{'Gfg' : 4, 'id' : 8, 'best': 11}]

# printing original list
print("The original list is : " + str(test_list))

# initializing key
del_key = 'id'

# Remove Key from Dictionary List
# Using loop + del
for items in test_list:
	if del_key in items:
		del items[del_key]

# printing result
print("The modified list : " + str(test_list))
