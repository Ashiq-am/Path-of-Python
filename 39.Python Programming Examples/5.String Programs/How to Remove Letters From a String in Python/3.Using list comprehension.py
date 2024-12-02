s = "hello world"

# Use a list comprehension to create a new string by joining
# characters that are not 'o' from original string 's'
s = "".join([c for c in s if c != "o"])
print(s)