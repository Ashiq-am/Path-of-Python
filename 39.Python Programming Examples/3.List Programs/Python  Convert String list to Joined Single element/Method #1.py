# Python3 code to demonstrate working of
# Convert String list to Joined Single element
# Using loop

# initializing list
test_list = ['gfg', 'is', 'best']

# printing original list
print("The original list is : " + str(test_list))

# initializing delim
delim = "-"

# Convert String list to Joined Single element
# Using loop
res = ''
for idx in range(len(test_list)-1):
	res = res + test_list[idx] + delim
if len(test_list) > 0:
		res = res + test_list[-1]
res = [res]

# printing result
print("String after performing join : " + str(res))
