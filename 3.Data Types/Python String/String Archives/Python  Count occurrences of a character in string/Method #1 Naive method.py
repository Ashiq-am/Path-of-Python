# Python3 code to demonstrate
# occurrence frequency using
# naive method

# initializing string
test_str = "GeeksforGeeks"

# using naive method to get count
# counting e
count = 0

for i in test_str:
	if i == 'e':
		count = count + 1

# printing result
print ("Count of e in GeeksforGeeks is : "
							+ str(count))
