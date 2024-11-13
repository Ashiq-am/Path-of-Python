import numpy as np

# Use a different approach to handle large integers
large_integer = np.int64(10) ** 20

try:
    # Perform the computation with large integers
    result = np.multiply(large_integer, large_integer, dtype=object)
    print(result)

except OverflowError as e:
    print(f"Overflow error occurred: {e}")
