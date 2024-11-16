# find if there is a substring such that it has
# the letter 'i' follwed by any small alphabet.
result = sr.str.contains(pat = 'i[a-z]', regex = True)

# print the result
print(result)
