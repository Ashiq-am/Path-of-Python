#define the function
def hollow_pyramid(rows):
	for i in range(rows):
		#print spaces
		for j in range(rows - i - 1):
			print(' ', end='')

		#print characters
		counter = 0
		for k in range(2 * i + 1):
			#print characters only in the start and end of row
			if k == 0 or k == 2 * i:
				print(chr(65 + counter), end='')
				counter += 1

			#print characters if it is the last row
			else:
				if i == rows - 1:
					print(chr(65 + counter), end='')
					counter += 1
				else:
					print(' ', end='')
		print()

#rows to be spanned
n = 7

#call the function
hollow_pyramid(n)
