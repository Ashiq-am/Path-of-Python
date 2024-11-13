# Python3 code to demonstrate
# occurrence frequency using
# lambda + sum() + map()

# initializing string
test_str = "GeeksforGeeks"

# using lambda + sum() + map() to get count
# counting e
count = sum(map(lambda x : 1 if 'e' in x else 0, test_str))

# printing result
print ("Count of e in GeeksforGeeks is : "
							+ str(count))
