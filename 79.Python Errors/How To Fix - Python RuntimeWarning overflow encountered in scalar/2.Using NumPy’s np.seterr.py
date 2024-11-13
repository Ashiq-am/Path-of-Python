import numpy as np

try:
    np.seterr(over='raise')
    result = np.array([1.0e308]) * 2  # This will trigger the warning
except RuntimeWarning as e:
    print(f"Output 3: {e}")
