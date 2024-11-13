# Python code to demonstrate
# to convert dictionary into string
# using str()

# initialising dictionary
test1 = { "testname" : "akshat",
		"test2name" : "manjeet",
		"test3name" : "nikhil"}

# print original dictionary
print (type(test1))
print ("initial dictionary = ", test1)

# convert dictionary into string
# using str
result = str(test1)

# print resulting string
print ("\n", type(result))
print ("final string = ", result)
