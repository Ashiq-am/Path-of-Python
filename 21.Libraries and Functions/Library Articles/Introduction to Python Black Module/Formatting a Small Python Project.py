import math

def calc_area(radius):return math.pi * radius ** 2

def display_area(radius):
  area = calc_area(radius)
  print(f"The area of a circle with radius {radius} is {area}")

display_area(5)
