# Python 3.9 code explaining
# str.removeprefix()

# String for removeprefix()
# If prefix exists then
# remove prefix from the string
# otherwise return original string

string1 = "Welcome to python 3.9"
print("Original String 1 : ", string1)

# prefix exists
result = string1.removeprefix("Welcome")
print("New string : ", result)

string2 = "Welcome Geek"
print("Original String 2 : ", string2)

# prefix doesn't exist
result = string2.removeprefix("Geek")
print("New string : ", result)
