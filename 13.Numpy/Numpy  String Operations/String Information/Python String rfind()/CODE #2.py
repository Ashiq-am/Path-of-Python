# Python program to demonstrate working of rfind()
# in a sub-string
word = 'geeks for geeks'

# Substring is searched in 'eeks for geeks'
print(word.rfind('ge', 2))

# Substring is searched in 'eeks for geeks'
print(word.rfind('geeks', 2))

# Substring is searched in 'eeks for geeks'
print(word.rfind('geeks ', 2))

# Substring is searched in 's for g'
print(word.rfind('for ', 4, 11))
