# Create a NumPy array of temperatures
temperatures = np.array([25, 30, 35, 40, 45])

# Create a boolean mask for temperatures above 35
mask = temperatures > 35

# Adjust the temperatures above 35 by subtracting 5
temperatures[mask] -= 5

print(temperatures)
