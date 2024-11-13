# Python code shows the working of
# .startsswith() function

text = "geeks for geeks."

# returns False
result = text.startswith('for geeks')
print (result)

# returns True
result = text.startswith('geeks')
print (result)

# returns False
result = text.startswith('for geeks.')
print (result)

# returns True
result = text.startswith('geeks for geeks.')
print (result)
