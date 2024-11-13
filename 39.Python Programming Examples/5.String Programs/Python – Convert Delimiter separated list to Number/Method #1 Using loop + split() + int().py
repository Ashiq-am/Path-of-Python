# Python3 code to demonstrate working of
# Convert Delimiter separated list to Number
# Using loop + split() + join()

# initializing string
test_str = "1@6@7@8@5@8@9"

# printing original string
print("The original string is : " + str(test_str))

# initializing Delimiter
delim = "@"

# spliting to get list of string numbers
temp = test_str.split(delim)
res = ''
for ele in temp:
	res = res + ele

# converting result into integer
res = int(res)

# printing result
print("Constructed integer : " + str(res))
