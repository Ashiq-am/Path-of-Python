# Python Program to find sum of square of first
# n natural numbers. This program avoids
# overflow upto some extent for large value
# of n.y

def squaresum(n):
	return (n * (n + 1) / 2) * (2 * n + 1) / 3

# main()
n = 4
print(squaresum(n))
