# Python code to demonstrate converting
# list into dictionary with none values
# using dict comprehension

# initializing list
ini_list = [1, 2, 3, 4, 5]

# printing intialized list
print ("initial list", str(ini_list))

# Converting list into dict()
res = {key: None for key in ini_list}

# printing final result
print ("final dictionary", str(res))
