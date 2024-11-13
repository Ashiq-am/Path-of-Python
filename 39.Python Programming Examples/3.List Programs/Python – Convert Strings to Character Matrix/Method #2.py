# Python3 code to demonstrate
# Convert Strings to Character Matrix
# using loop + list()

# Initializing list
test_list = ['gfg', 'is', 'best']

# printing original list
print("The original list is : " + str(test_list))

# Convert Strings to Character Matrix
# using loop + list()
res = []
for sub in test_list:
	res.append(list(sub))

# printing result
print ("List String after conversion to Matrix : " + str(res))
