# A O(sqrt(n)) program that prints all divisors
# in sorted order
from math import *

# Function to print the divisors
def printDivisors (n):

	i = 1
	while (i * i < n):
		if (n % i == 0):
			print(i, end = " ")

		i += 1

	for i in range(int(sqrt(n)), 0, -1):
		if (n % i == 0):
			print(n // i, end = " ")

# Driver Code
print("The divisors of 100 are: ")

printDivisors(100)

