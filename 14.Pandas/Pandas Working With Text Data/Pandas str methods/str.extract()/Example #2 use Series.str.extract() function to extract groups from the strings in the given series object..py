# extract groups having any capital letter
# followed by 'i' and any other character
import sr as sr

result = sr.str.extract(pat = '([A-Z]i.)')

# print the result
print(result)
