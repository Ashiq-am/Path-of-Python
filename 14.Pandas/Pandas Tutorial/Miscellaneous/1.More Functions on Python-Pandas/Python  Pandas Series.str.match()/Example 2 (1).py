# match groups having any capital letter
# followed by 'i' and any other character
result = sr.str.match(pat = '([A-Z]i.)')

# print the result
print(result)
