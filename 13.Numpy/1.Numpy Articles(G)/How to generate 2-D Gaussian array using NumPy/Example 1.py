# Importing Numpy package
import numpy as np

# Initializing value of x-axis and y-axis
# in the range -1 to 1
x, y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
dst = np.sqrt(x*x+y*y)

# Intializing sigma and muu
sigma = 1
muu = 0.000

# Calculating Gaussian array
gauss = np.exp(-( (dst-muu)**2 / ( 2.0 * sigma**2 ) ) )

print("2D Gaussian array :\n")
print(gauss)
