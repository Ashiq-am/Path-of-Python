# Python code to illustrate the working of strip()
string = ' Geeks for Geeks '

# Leading spaces are removed
print(string.strip())

# Geeks is removed
print(string.strip(' Geeks'))

# Not removed since the spaces do not match
print(string.strip('Geeks'))
