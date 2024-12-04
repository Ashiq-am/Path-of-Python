s1 = "Python"

# Index of the character to remove
idx = 3
# Convert string to a list

li = list(s1)
# Remove the character at the specified index

li.pop(idx)
# Join the list back into a string
res = ''.join(li)
print(res)