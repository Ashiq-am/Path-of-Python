# Python3 program to Convert list of
# sequential number into intervals

def interval_extract(list):
	length = len(list)
	i = 0
	while (i< length):
		low = list[i]
		while i <length-1 and list[i]+1 == list[i + 1]:
			i += 1
		high = list[i]
		if (high - low >= 1):
			yield [low, high]
		elif (high - low == 1):
			yield [low, ]
			yield [high, ]
		else:
			yield [low, ]
		i += 1

# Driver code
l = [2, 3, 4, 5, 7, 8, 9, 11, 15, 16]
print( list(interval_extract(l)))
