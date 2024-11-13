# Python 3 program to find the volume
# of a tetrahedron
import math

# Function to calculate volume
def vol_tetra(side):

	volume = (pow(side, 3) / (6 * math.sqrt(2)))
	return volume

# Driver Code
if __name__ == "__main__":

	side = 3
	vol = vol_tetra(side)
	print(round(vol, 2))
