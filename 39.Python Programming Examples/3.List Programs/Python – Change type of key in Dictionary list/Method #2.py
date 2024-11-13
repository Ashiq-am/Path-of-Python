# Python3 code to demonstrate working of
# Change type of key in Dictionary list
# Using list comprehension

# initializing list
test_list = [{'gfg' : 1, 'is' : '56', 'best' : (1, 2)},
			{'gfg' : 5, 'is' : '12', 'best' : (6, 2)},
			{'gfg' : 3, 'is' : '789', 'best' : (7, 2)}]

# printing original list
print("The original list is : " + str(test_list))

# initializing change key
chnge_key = 'is'

# Change type of key in Dictionary list
# Using list comprehension
res = [{key : (int(val) if key == chnge_key else val)
						for key, val in sub.items()}
						for sub in test_list]

# printing result
print("The converted Dictionary list : " + str(res))
