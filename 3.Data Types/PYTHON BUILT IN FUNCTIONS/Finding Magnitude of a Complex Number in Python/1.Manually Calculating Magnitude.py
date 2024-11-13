#Manually calculating magnitude
def magnitude_manual(z):
	return (z.real**2 + z.imag**2)**0.5

# Example
complex_number = 3 + 4j
result = magnitude_manual(complex_number)
print(f"Manually calculated magnitude: {result}")
