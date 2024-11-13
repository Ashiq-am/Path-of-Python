# Python program to illustrate
# counting number of alphabets
# using isalpha()

# Given string
string='Ayush Saxena'
count=0

# Initialising new strings
newstring1 =""
newstring2 =""

# Iterating the string and checking for alphabets
# Incrementing the counter if an alphabet is found
# Finally printing the count
for a in string:
	if (a.isalpha()) == True:
		count+=1
		newstring1+=a
print(count)
print(newstring1)

#Given string
string='Ayush0212'
count=0
for a in string:
	if (a.isalpha()) == True:
		count+=1
		newstring2+=a
print(count)
print(newstring2)
