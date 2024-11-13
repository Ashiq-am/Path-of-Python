import math

def cylinder_surface_area(radius, height):
	return 2 * math.pi * radius**2 + 2 * math.pi * radius * height

def cylinder_volume(radius, height):
	return math.pi * radius**2 * height

# Example usage:
radius = 5
height = 10

surface_area = cylinder_surface_area(radius, height)
volume = cylinder_volume(radius, height)

print(f"Surface Area: {surface_area}")
print(f"Volume: {volume}")
