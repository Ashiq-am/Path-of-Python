import cmath

# Using cmath module
def magnitude_cmath(z):
	return cmath.polar(z)[0]

# Example
complex_number = 3 + 4j
result = magnitude_cmath(complex_number)
print(f"Magnitude using cmath: {result}")
