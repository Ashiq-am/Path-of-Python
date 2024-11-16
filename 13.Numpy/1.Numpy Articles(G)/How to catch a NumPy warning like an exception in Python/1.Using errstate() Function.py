# Import the numpy library
import numpy as np

# Create a numpy array
arr = np.array([1,5,4])

# Divide by Zero Exception
with np.errstate(invalid='raise'):
    try:
        arr / 0
    except FloatingPointError:
        print('Error: Division by Zero')
