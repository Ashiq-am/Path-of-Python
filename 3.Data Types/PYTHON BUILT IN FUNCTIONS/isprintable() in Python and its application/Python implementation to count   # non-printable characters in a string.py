# Python implementation to count
# non-printable characters in a string

# Given string and new string
string ='GeeksforGeeks\nname\nis\nCS portal'
newstring = ''

# Initialising the counter to 0
count = 0

# Iterating the string and
# checking for non-printable characters
# Incrementing the counter if a
# non-printable character is found
# and replacing it by space in the newstring

# Finally printing the count and newstring

for a in string:
	if (a.isprintable()) == False:
			count+= 1
			newstring+=' '
	else:
			newstring+= a
print(count)
print(newstring)
