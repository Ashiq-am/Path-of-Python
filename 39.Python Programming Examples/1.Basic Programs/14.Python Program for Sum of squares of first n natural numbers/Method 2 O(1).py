# Python3 Program to
# find sum of square
# of first n natural
# numbers

# Return the sum of
# square of first n
# natural numbers
def squaresum(n) :
	return (n * (n + 1) * (2 * n + 1)) // 6

# Driven Program
n = 4
print(squaresum(n))


