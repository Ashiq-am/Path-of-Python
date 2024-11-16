# importing the module
import numpy as np

# taking the celsius input
inp = [0, 12, 45.21, 34, 99.91]

# storing the input
# in numpy array
cel = np.array(inp)

print(f"Celsius {cel}")

# using formulae
feh = (9 * cel / 5 + 32)

# printing results
print(f"Fahrenheit {feh}")
