# Python3 code to demonstrate working of
# Custom space size padding in Strings List
# Using loop

# initializing lists
test_list = ["Gfg", "is", "Best"]

# printing original list
print("The original list is : " + str(test_list))

# initializing padding numbers
lead_size = 3
trail_size = 2

res = []
for ele in test_list:

	# * operator handles number of spaces
	res.append((lead_size * ' ') + ele + (trail_size * ' '))

# printing result
print("Padded Strings : " + str(res))
