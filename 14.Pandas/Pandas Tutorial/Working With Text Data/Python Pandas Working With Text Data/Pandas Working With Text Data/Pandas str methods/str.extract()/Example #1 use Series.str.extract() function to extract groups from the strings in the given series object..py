# extract groups having a vowel followed by
# any character
import sr as sr

result = sr.str.extract(pat = '([aeiou].)')

# print the result
print(result)
