# Python program to convert a list to string using list comprehension
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# using list comprehension
listToStr = ' '.join([str(elem) for elem in s])

print(type(s[2]))
print(listToStr)
print(type(listToStr[2]))
