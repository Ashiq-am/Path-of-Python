# Python3 code to demonstrate working of
# Unique Values of Key in Dictionary
# Using list comprehension

# initializing list
test_list = [{'Gfg' : 5, 'is' : 6, 'best' : 7, 'for' : 8, 'geeks' : 10},
			{'Gfg' : 9, 'is' : 4, 'best' : 7, 'for' : 4, 'geeks' :7},
			{'Gfg' : 2, 'is' : 10, 'best' : 8, 'for' : 9, 'geeks' : 3}]

# printing original list
print("The original list is : " + str(test_list))

# initializing key
op_key = 'best'

# Unique Values of Key in Dictionary
# Using list comprehension
res = list(set(sub[op_key] for sub in test_list))

# printing result
print("The unique values of key : " + str(res))
