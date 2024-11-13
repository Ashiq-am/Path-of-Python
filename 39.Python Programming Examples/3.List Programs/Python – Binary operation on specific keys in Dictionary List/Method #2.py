# Python3 code to demonstrate working of
# Binary operation on specific keys in Dictionary List
# Using list comprehension + enumerate()

# initializing list
test_list = [{'Gfg' : 5, 'is' : 6, 'best' : 7, 'for' : 8, 'geeks' : 10},
			{'Gfg' : 9, 'is' : 4, 'best' : 10, 'for' : 4, 'geeks' :7},
			{'Gfg' : 2, 'is' : 10, 'best' : 8, 'for' : 9, 'geeks' : 3}]

# printing original list
print("The original list is : " + str(test_list))

# initializing keys
op1_key = 'Gfg'
op2_key = 'best'

# Binary operation on specific keys in Dictionary List
# Using list comprehension + enumerate()
res = [(idx, val[op1_key] * val[op2_key]) for idx, val in enumerate(test_list)]

# printing result
print("The constructed result list : " + str(res))
