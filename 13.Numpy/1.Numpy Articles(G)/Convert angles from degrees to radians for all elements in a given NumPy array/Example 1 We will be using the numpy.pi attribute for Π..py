# importing the module
import numpy as np

# creating an array containing angles in radians
rad = np.array([np.pi, np.pi / 4,
				np.pi / 2, 3 * np.pi / 2,
				2 * np.pi])
print("The angles in radian")
print(rad)

# converting array from radian to degree
deg = np.rad2deg(rad)
print("\nThe angles in degree")
print(deg)
