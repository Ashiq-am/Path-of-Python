# Python3 code to demonstrate working of
# Convert List to delimiter separated String
# Using loop + str()

# initializing list
test_list = [7, "Gfg", 8, "is", "best", 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing delim
delim = "*"

res = ''

# using loop to add string followed by delim
for ele in test_list:
	res = res + str(ele) + delim

# printing result
print("The resultant string : " + str(res))
