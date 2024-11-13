# 2x3 - 6x2 + 2x - 1 for x = 3
poly = [2, -6, 2, -1]
x = 3
n = len(poly)

# Declaring the result
result = 0

# Running a for loop to traverse through the list
for i in range(n):

	# Declaring the variable Sum
	Sum = poly[i]

	# Running a for loop to multiply x (n-i-1)
	# times to the current coefficient
	for j in range(n - i - 1):
		Sum = Sum * x

	# Adding the sum to the result
	result = result + Sum

# Printing the result
print(result)
