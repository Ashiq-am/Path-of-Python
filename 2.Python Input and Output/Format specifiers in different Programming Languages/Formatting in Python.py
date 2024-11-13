# Python program to illustrate
# format specifiers in Python

str = "GeeksforGeeks"
str1 = "Welcome to"

# Unformatted Output in Python
print("Welcome to GfG !")

# Unformatted Output using separator
# print("Welcome to GfG !", sep = ", ")
print(str1, str, sep = ", ")

# String Formatting
print("Welcome to % s !" % str)

# String Formatting
name = "GfG"
age = 4
print("% s is % d years old." % (name, age))

# Formatting using format()
print("Hey, Welcome to {}!".format(str, age))
