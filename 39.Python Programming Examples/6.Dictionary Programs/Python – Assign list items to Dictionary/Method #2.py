# Python3 code to demonstrate working of
# Assign list items to Dictionary
# Using list comprehension + zip()

# initializing list
test_list = [{'Gfg' : 1, 'id' : 2 },
			{'Gfg' : 4, 'id' : 4 }]

# printing original list
print("The original list is : " + str(test_list))

# initializing key
new_key = 'best'

# initializing list
add_list = [12, 2]

# Assign list items to Dictionary
# Using list comprehension + zip()
res = [{**sub, new_key : ele} for sub, ele in zip(test_list, add_list)]

# printing result
print("The modified dictionary : " + str(res))
