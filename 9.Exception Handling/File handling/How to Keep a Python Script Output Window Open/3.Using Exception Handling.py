# Using exception handling
try:
    print("Hello, World!")
    raise KeyboardInterrupt  # Simulating a keyboard interrupt
except KeyboardInterrupt:
    input("Press Enter to exit...")