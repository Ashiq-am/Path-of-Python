# Python3 code to demonstrate working of
# Check if string repeats itself
# Using list slicing + find()

# initializing string
test_str = "GeeksforGeeksGeeksforGeeksGeeksforGeeks"

# printing original string
print("The original string is : " + test_str)

# using list slicing + find()
# Check if string repeats itself
res = None
temp = (test_str + test_str).find(test_str, 1, -1)
if temp != -1:
	res = test_str[:temp]

# printing result
print("The root substring of string : " + res)
