# Python3 code to demonstrate working of
# Convert String Records to Tuples Lists
# Using loop + eval()

# initializing string
test_str = '[(gfg, ), (is, ), (best, )]'

# printing original string
print("The original string is : " + test_str)

# Convert String Records to Tuples Lists
# Using loop + eval()
res = ''
temp = True
for chr in test_str:
	if chr == '(' and temp:
		res += '("'
		temp = False
		continue
	if chr == ', ' and not temp:
		res += '"'
		temp = True
	res += chr
res = eval(res)

# printing result
print("The list of Tuples is : " + str(res))
