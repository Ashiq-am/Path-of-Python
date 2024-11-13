# Python3 code to demonstrate working of
# Filter key's value from other key
# Using loop

# initializing list
test_list = [{'gfg' : 5, 'is' : 8, 'best' : 12},
			{'gfg' : 7, 'is' : 12, 'best' : 24},
			{'gfg' : 20, 'is' : 17, 'best' : 18}]

# printing original list
print("The original list is : " + str(test_list))

# initializing required key
req_key = 'gfg'

# initializing filter key
fil_key = 'best'

# initializing filter val
fil_val = 24

# Filter key's value from other key
# Using loop
res = []
for sub in test_list:


    if sub[fil_key] == fil_val:
        res.append(sub[req_key])

# printing result
print("The required value : " + str(res))
