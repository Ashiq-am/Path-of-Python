# Python Program to Demonstrate the strings
# methods to check whether given Character
# is in uppercase or lowercase with the help
# of ASCII values

# Input by geeks
x = "GEeK"

# counter
counter = 0

for char in x:
    if (ord(char) >= 65 and ord(char) <= 90):
        counter = counter + 1

    # Check for the condition
    # if the ASCII value is Between 97 and 122
    # if condition is True print the
    # corresponding result
    if (ord(char) >= 97 and ord(char) <= 122):
        print("Lower Character found")
        break
if counter == len(x):
    print(True)
