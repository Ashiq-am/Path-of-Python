# Python code to demonstrate
# to get characters in a string
# if present

# initialising string
ini_string = "123()#$ABGFDabcjw"

# printing string and its length
print ("initial string : ", ini_string)

# code to find characters in string
res1 = ""
for i in ini_string:
	if i.isalpha():
		res1 = "".join([res1, i])


# printing resultant string
print ("first result: ", str(res1))
