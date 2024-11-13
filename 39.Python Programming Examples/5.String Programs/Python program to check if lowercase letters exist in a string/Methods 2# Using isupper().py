# Python Program to demonstrate the
# is.upper() method in strings
# Take a string
str = "GEEKS"

# Traversing Each character
# to check whether it is in uppercase
for char in str:
    k = char.isupper()
    if k == False:
        print('False')

        # Break the Loop
        # when you get any
        # uppercase character.
        break

# Default condition if the string
# does not have any uppercase character.
if (k == 1):
    print('True')
