from functools import reduce

# Lambda function to calculate the area
def area_lambda(length, width):
	return reduce(lambda x, y: x * y, [length, width])

# Example usage:
length = 5
width = 8
result = area_lambda(length, width)
print(f"Area of Rectangle: {result}")
