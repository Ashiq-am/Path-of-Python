# importing
import numpy as np

# Real number is created using the
# np.outer method
real_part = np.outer(np.ones((3,)), np.linspace(1, 3, 3))
print("The real part ")
print(real_part)

# imaginary number is created using the
# np.outer method
imaginary_part = np.outer(1j*np.linspace(3, 6, 3), np.ones((3,)))
print("The imaginary part")
print(imaginary_part)

# Forming a grid by combainaing rael
# and imaginary part
mandelbrot_grid = real_part + imaginary_part
print("Mandelbrot grid")
print(mandelbrot_grid)
