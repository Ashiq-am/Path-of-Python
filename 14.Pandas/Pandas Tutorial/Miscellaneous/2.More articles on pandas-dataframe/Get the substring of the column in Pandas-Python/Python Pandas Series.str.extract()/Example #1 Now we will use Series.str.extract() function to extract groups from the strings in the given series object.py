# extract groups having a vowel followed by
# any character
result = sr.str.extract(pat = '([aeiou].)')

# print the result
print(result)
