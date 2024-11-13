# Python3 code to demonstrate working of
# Convert Float String List to Float Values
# Using map() + float()

# initializing list
test_list = ['87.6', '454.6', '9.34', '23', '12.3']

# printing original list
print("The original list : " + str(test_list))

# Convert Float String List to Float Values
# Using map() + float()
res = list(map(float, test_list))

# printing result
print("List after conversion : " + str(res))
