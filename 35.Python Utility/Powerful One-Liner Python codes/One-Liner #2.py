# Input for row and column
R = int(input())
C = int(input())

matrix = []

# for loop for row entries
for i in range(R):
	a =[]

	# for loop for column entries
	for j in range(C):
		a.append(int(input()))
	matrix.append(a)
