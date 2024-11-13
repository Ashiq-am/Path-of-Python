# Python3 code to demonstrate working of
# Get values of particular key in list of dictionaries
# Using list comprehension

# initializing list
test_list = [{'gfg' : 1, 'is' : 2, 'good' : 3},
			{'gfg' : 2}, {'best' : 3, 'gfg' : 4}]

# printing original list
print("The original list is : " + str(test_list))

# Using list comprehension
# Get values of particular key in list of dictionaries
res = [ sub['gfg'] for sub in test_list ]

# printing result
print("The values corresponding to key : " + str(res))
