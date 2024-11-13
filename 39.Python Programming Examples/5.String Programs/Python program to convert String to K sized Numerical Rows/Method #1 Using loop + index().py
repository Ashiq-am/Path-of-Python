# initializing string
test_str = 'geeksforgeekscse'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

alphabs = "abcdefghijklmnopqrstuvwxyz"

res = []
temp = []
for ele in test_str:

	# finding numerical position using index()
	temp.append(alphabs.index(ele))

	# regroup on K
	if len(temp) == K:
		res.append(temp)
		temp = []

# appending remaining characters
if temp != []:
	res.append(temp)

# printing result
print("Grouped and Converted String : " + str(res))
