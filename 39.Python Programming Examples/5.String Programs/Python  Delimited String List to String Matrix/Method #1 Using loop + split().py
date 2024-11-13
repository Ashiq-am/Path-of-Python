# Python3 code to demonstrate working of
# Delimited String List to String Matrix
# Using loop + split()

# initializing list
test_list = ['gfg:is:best', 'for:all', 'geeks:and:CS']

# printing original list
print("The original list is : " + str(test_list))

# Delimited String List to String Matrix
# Using loop + split()
res = []
for sub in test_list:
	res.append(sub.split(':'))

# printing result
print("The list after conversion : " + str(res))
