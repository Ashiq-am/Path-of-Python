# Python program to count the items
# until a list is encountered
def Count(li):
	counter = 0
	for num in li:
		if isinstance(num, tuple):
			break
		counter = counter + 1
	return counter

# Driver Code
li = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
print(Count(li))
