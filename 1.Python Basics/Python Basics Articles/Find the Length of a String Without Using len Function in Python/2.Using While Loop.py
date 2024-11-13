# Returns length of string
def findLen(str):
	counter = 0
	while str[counter:]:
		counter += 1
	return counter


str = "geeksforgeeks"
print(findLen(str))
