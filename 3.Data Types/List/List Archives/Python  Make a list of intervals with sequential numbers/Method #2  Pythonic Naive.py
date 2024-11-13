# Python3 program to Convert list of
# sequential number into intervals

def interval_extract(list):
	list = sorted(set(list))
	range_start = previous_number = list[0]

	for number in list[1:]:
		if number == previous_number + 1:
			previous_number = number
		else:
			yield [range_start, previous_number]
			range_start = previous_number = number
	yield [range_start, previous_number]

# Driver code
l = [2, 3, 4, 5, 7, 8, 9, 11, 15, 16]
print( list(interval_extract(l)))
