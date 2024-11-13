import math

# Using math module
def magnitude_math(z):
	return math.sqrt(pow(z.real, 2) + pow(z.imag, 2))

# Example
complex_number = 3 + 4j
result = magnitude_math(complex_number)
print(f"Magnitude using pow() module: {result}")
