str1 = ''
str2 = 'Ashiqul'

# repr is used to print the string along with the quotes

# Returns str1
print(repr(str1 and str2))

# Returns str1
print(repr(str2 and str1))

# Returns str2
print(repr(str1 or str2))

# Returns str2
print(repr(str2 or str1))

str1 = 'Amin'

# Returns str2
print(repr(str1 and str2))

# Returns str1
print(repr(str2 and str1))

# Returns str1
print(repr(str1 or str2))

# Returns str2
print(repr(str2 or str1))

str1='Ashiq'

# Returns False
print(repr(not str1))

str1 = ''

# Returns True
print(repr(not str1))
