s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

listToStr = ' '.join([str(elem) for i,elem in enumerate(s)])

print(type(s[2]))
print(listToStr)
print(type(listToStr[2]))
