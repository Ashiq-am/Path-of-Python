# Python program to illustrate
# counting number of alphabets
# using isalpha()

# Given string
string='Ayush Saxena'
count=0

# Initialising new strings
new_string1 =""
new_string2 =""

# Iterating the string and checking for alphabets
# Incrementing the counter if an alphabet is found
# Finally printing the count
for a in string:
	if (a.isalpha()) == True:
		count+=1
		new_string1+=a
print(count)
print(new_string1)

#Given string
string='Ayush0212'
count=0
for a in string:
	if (a.isalpha()) == True:
		count+=1
		new_string2+=a
print(count)
print(new_string2)
