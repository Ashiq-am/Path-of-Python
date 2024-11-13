# Python program to illustrate
# application of isdigit()
# initialising Empty string
newstring = ''

# Initialising the counters to 0
count = 0

# Incrementing the counter if a digit is found
# and adding the digit to a new string
# Finally printing the count and the new string

for a in range(53):
    b = chr(a)
    if b.isdigit() == True:
        count += 1
        newstring += b

print("Total digits in range :", count)
print("Digits :", newstring)
