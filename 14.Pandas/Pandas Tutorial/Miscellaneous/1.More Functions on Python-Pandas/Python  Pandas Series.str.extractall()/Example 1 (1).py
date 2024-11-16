# extract all groups having a vowel followed by
# any character
result = sr.str.extractall(pat = '([aeiou].)')

# print the result
print(result)
