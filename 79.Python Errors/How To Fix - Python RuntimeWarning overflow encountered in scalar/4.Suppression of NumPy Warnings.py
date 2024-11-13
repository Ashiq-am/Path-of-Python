import numpy as np

try:
    # Set NumPy to ignore overflow warnings
    np.seterr(over='ignore')

    # Perform the computation
    result = np.array([1.0e308]) * 2

    # Print the result
    print("Result:", result)

except RuntimeWarning as e:
    # If a RuntimeWarning occurs, print the warning message
    print(f"RuntimeWarning: {e}")
