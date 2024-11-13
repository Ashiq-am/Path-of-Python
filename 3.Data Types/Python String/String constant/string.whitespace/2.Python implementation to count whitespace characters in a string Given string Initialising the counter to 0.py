# Python implementation to count whitespace characters in a string
# Given string
# Initialising the counter to 0
string = 'My name is Ayush'
count=0

# Iterating the string and checking for whitespace characters
# Incrementing the counter if a whitespace character is found
# Finally printing the count
for a in string:
	if (a.isspace()) == True:
		count+=1
print(count)

string = 'My name is \n\n\n\n\nAyush'
count = 0
for a in string:
	if (a.isspace()) == True:
		count+=1
print(count)
