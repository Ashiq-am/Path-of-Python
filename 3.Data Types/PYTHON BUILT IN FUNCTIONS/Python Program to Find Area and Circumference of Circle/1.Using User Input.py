import math

# Taking radius input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculating area and circumference
area = math.pi * radius**2
circumference = 2 * math.pi * radius

# Displaying the results
print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")
