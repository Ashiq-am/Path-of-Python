# Python3 code to demonstrate working of
# Extract Preceeding Record
# Using list comprehension + enumerate()

# initializing list
test_list = [('Gfg', 3), ('is', 4), ('best', 1), ('for', 10), ('geeks', 11)]

# printing original list
print("The original list is : " + str(test_list))

# initializing Key
key = 'for'

# Extract Preceding Record
# Using list comprehension + enumerate()
res = [(test_list[idx - 1][0], test_list[idx - 1][1])
	for idx, (x, y) in enumerate(test_list) if x == key and idx > 0]

# printing result
print("The Preceeding record : " + str(res))
