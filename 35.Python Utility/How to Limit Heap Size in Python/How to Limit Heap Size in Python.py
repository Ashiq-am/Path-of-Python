import resource
import sys

# Set maximum heap size (e.g., 500 MB)
max_heap_size = 500 * 1024 * 1024  # 500 MB in bytes

# Set memory limit
resource.setrlimit(resource.RLIMIT_AS, (max_heap_size, max_heap_size))

try:
    # Simulate a memory-heavy operation
    print("Allocating memory...")
    large_list = [0] * (10**8)  # This will consume significant memory
except MemoryError:
    print("Memory limit reached! Exiting gracefully.")
    sys.exit(1)

print("Memory allocation successful within limit.")
