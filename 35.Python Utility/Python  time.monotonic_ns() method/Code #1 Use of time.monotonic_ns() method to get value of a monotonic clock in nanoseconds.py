# Python program to explain time.monotonic_ns() method

# importing time module
import time

# Get the value of
# the monotonic clock in
# fractional seconds using
# time.monotonic() method
value1 = time.monotonic()

# Get the value of
# the monotonic clock in
# nanoseconds using
# time.monotonic_ns() method
value2 = time.monotonic_ns()

# print the value of
# the monotonic clock (in fractional seconds)
print("Value of the monotonic clock (in fractional seconds):", value1)

# print the value of
# the monotonic clock (in nanoseconds)
print("Value of the monotonic clock (in nanoseconds):", value2)
