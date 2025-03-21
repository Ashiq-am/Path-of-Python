""""""


"""Equivalent to 1 / 2 * (np.exp(x) - np.exp(-x)) or -1j * np.sin(1j * x)."""

# Python3 program explaining
# sinh() function

import numpy as np
import math

in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print("Input array : \n", in_array)

Sinh_Values = np.sinh(in_array)
print("\nSine Hyperbolic values : \n", Sinh_Values)