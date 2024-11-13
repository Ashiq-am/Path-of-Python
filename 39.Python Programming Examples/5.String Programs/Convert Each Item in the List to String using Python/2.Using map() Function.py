# Python program to convert a list to string map

s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# using map comprehension
listToStr = ' '.join(map(str, s))

print(type(s[2]))
print(listToStr)
print(type(listToStr[2]))
