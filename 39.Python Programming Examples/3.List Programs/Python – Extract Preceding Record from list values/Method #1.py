# Python3 code to demonstrate working of
# Extract Preceeding Record
# Using zip() + enumerate() + loop

# initializing list
test_list = [('Gfg', 3), ('is', 4), ('best', 1), ('for', 10), ('geeks', 11)]

# printing original list
print("The original list is : " + str(test_list))

# initializing Key
key = 'for'

# Extract Preceding Record
# Using zip() + enumerate() + loop
for idx, (a, b) in enumerate(zip(test_list, test_list[1:])):
	if b[0] == key:
		res = (a[0], a[1])

# printing result
print("The Preceeding record : " + str(res))
