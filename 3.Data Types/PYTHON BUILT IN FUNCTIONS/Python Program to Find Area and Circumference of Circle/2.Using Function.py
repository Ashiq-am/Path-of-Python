import math

# Function to calculate area and circumference with default radius
def calculate(radius=1.0):
	area = math.pi * radius**2
	circumference = 2 * math.pi * radius
	return area, circumference

# Example usage with default radius
default_area, default_circumference = calculate()
print(f"Default Area: {default_area}")
print(f"Default Circumference: {default_circumference}")
