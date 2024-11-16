# importing the module
import numpy as np

# creating an array containing angles in radians
rad = np.array([3.14159265, 0.78539816,
				1.57079633, 4.71238898,
				6.28318531])
print("The angles in radian")
print(rad)

# converting array from radian to degree
deg = []
for angle in rad:
	deg.append(round(angle * (180 / np.pi)))
print("\nThe angles in degree")
print(deg)
