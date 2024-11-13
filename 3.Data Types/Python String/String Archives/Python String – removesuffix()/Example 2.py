# Python 3.9 code explaining
# str.removesuffix()

# String for removesuffix()
# If suffix exists then
# then it remove suffix from the string
# otherwise return original string

string1 = "Welcome to python 3.9"
print("Original String 1 : ", string1)

# suffix exists
result = string1.removesuffix("3.9")
print("New string : ", result)

string2 = "Welcome Geek"
print("Original String 2 : ", string2)

# suffix doesn't exist
result = string2.removesuffix("Welcome")
print("New string : ", result)
