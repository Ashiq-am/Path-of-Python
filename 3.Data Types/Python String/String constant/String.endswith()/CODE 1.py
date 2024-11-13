# Python code shows the working of
# .endswith() function

text = "geeks for geeks."

# returns False
result = text.endswith('for geeks')
print (result)

# returns True
result = text.endswith('geeks.')
print (result)

# returns True
result = text.endswith('for geeks.')
print (result)

# returns True
result = text.endswith('geeks for geeks.')
print (result)
