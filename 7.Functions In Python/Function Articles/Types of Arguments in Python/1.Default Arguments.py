def calculate_area(length, width=5):
    area = length * width
    print(f"Area of rectangle: {area}")
# Driver code (We call calculate_area() with only
# the length argument)
calculate_area(10)
# We can also pass a custom width
calculate_area(10, 8)