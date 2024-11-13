# Lambda function to calculate the area
def area_trapezoid_lambda(base1, base2, height): return (
	base1 + base2) / 2 * height

# Driver code
base1 = 5
base2 = 9
height = 4
result = area_trapezoid_lambda(base1, base2, height)
print(f"Area of Trapezoid: {result}")
