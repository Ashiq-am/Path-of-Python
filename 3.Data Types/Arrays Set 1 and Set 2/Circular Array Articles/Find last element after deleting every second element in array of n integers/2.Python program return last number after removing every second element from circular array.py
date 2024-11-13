# Find the value nearest
# to power of 2
import math
def nearestPowerof2(n):

	p = int(math.log2(n))
	return p

# Eliminate n
def circularElimination(n):

	# power of 2
	power = nearestPowerof2(n)
	result = (1 + 2 *
			(n - pow(2,power)))
	return result

n = 5

# Driver code
# Function call
result = circularElimination(n)
print(result)
n = 10
result = circularElimination(n)
print(result)
