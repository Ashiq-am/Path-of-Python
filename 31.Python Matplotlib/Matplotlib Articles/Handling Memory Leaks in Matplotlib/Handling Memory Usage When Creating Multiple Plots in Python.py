import matplotlib.pyplot as plt
import numpy as np
import psutil
import os

def memory_usage():
    """Check the memory usage of the current process."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Memory in MB

print("Memory usage before creating plots (MB):", memory_usage())
for i in range(1000):  # Creating 1000 figures
    x = np.linspace(0, 10, 100)
    y = np.sin(x + i / 100.0)
    plt.figure()
    plt.plot(x, y)
    plt.title(f"Plot {i+1}")
    # Not closing the figure, leading to memory accumulation

print("Memory usage after creating plots without closing (MB):", memory_usage())

# Now properly close figures after use
print("\nMemory usage before proper cleanup (MB):", memory_usage())
for i in range(1000):  # Creating 1000 figures again
    x = np.linspace(0, 10, 100)
    y = np.sin(x + i / 100.0)
    plt.figure()
    plt.plot(x, y)
    plt.title(f"Plot {i+1}")
    plt.close()  # Close the figure to release memory

print("Memory usage after closing figures (MB):", memory_usage())
