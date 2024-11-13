# Python code to demonstrate
# converting list into dictionary with none values
# using zip() and dictionary

# initializing list
ini_list = [1, 2, 3, 4, 5]

# printing intialized list
print ("initial list", str(ini_list))

# Converting list into dictionary using zip() and dictionary
res = dict(zip(ini_list, [None]*len(ini_list)))

# printing final result
print ("final dictionary", str(res))
