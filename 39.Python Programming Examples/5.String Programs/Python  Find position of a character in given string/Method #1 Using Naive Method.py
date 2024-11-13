# Python3 code to demonstrate
# to find the first position of the character
# in a given string

# Initialising string
ini_string = 'abcdef'

# Character to find
c = "b"
# printing initial string and character
print("initial_string : ", ini_string, "\ncharacter_to_find : ", c)

# Using Naive Method
res = None
for i in range(0, len(ini_string)):
    if ini_string[i] == c:
        res = i + 1
        break

if res == None:
    print("No such charater available in string")
else:
    print("Character {} is present at {}".format(c, str(res)))
