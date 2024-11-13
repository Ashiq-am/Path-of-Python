#define the function
def left_pascal(rows):
	#ascending part of the pattern
	for i in range(1, rows + 1):
		for j in range(1, i + 1):
			print(chr(64 + j), end="")
		print()

	#descending part of the pattern
	for i in range(rows - 1, 0, -1):
		for j in range(1, i + 1):
			print(chr(64 + j), end="")
		print()

#rows to be spanend
n = 7

#call the function
left_pascal(n)
