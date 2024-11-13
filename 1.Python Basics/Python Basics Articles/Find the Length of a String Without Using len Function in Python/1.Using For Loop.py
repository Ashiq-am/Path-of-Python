# Returns length of string
def findLen(str):
	counter = 0
	for i in str:
		counter += 1
	return counter


str = "geeksforgeeks"
print(findLen(str))
