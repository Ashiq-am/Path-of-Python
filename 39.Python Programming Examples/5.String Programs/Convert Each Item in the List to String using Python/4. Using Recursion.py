def list_to_string(lst):
	if not lst:
		return []
	return [str(lst[0])] + list_to_string(lst[1:])

s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listToStr = list_to_string(s)

print(type(s[2]))
print(listToStr)
print(type(listToStr[2]))
