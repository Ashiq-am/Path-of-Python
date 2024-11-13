# Python program to verify IP without using RegEx

# explicit function to verify IP
def isValidIP(s):

	# initialize counter
	counter = 0

	# check if period is present
	for i in range(0, len(s)):
		if(s[i] == '.'):
			counter = counter+1
	if(counter != 3):
		return 0

	# check the range of numbers between periods
	st = set()
	for i in range(0, 256):
		st.add(str(i))
	counter = 0
	temp = ""
	for i in range(0, len(s)):
		if(s[i] != '.'):
			temp = temp+s[i]
		else:
			if(temp in st):
				counter = counter+1
			temp = ""
	if(temp in st):
		counter = counter+1

	# verifying all conditions
	if(counter == 4):
		return 'Valid Ip address'
	else:
		return 'Invalid Ip addess'


# Driver Code
print(isValidIP('110.234.52.124'))
