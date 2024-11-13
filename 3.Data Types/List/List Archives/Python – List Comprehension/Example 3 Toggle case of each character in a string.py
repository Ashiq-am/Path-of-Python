# Initializing string
string = 'Geeks4Geeks'

# Toggle case of each character
List = list(map(lambda i: chr(ord(i)^32), string))

# Display list
print(List)
