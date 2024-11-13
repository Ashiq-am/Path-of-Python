# Python implementation to count numeric characters
# in a string and print non numeric characters
# Given string
# Initialising the counter to 0
string = '123geeks456for789geeks'
count = 0

newstring1 = ""
newstring2 = ""

# Iterating the string and checking for numeric characters
# Incrementing the counter if a numeric character is found
# And adding the character to new string if not numeric
# Finally printing the count and the newstring
for a in string:
    if (a.isnumeric()) == True:
        count += 1
    else:
        newstring1 += a
print(count)
print(newstring1)

string = '123ayu456'
count = 0
for a in string:
    if (a.isnumeric()) == True:
        count += 1
    else:
        newstring2 += a
print(count)
print(newstring2)
