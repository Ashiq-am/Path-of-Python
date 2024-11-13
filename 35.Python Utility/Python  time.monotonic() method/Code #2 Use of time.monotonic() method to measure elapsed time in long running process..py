# Python program to explain time.monotonic() method

# importing time module
import time

# Get the value of
# a monotonic clock at the
# beginning of the process
# using time.monotonic() method
start = time.monotonic()

# print the value of
# the monotonic clock
print("At the beginning of the process")
print("Value of the monotonic clock (in fractional seconds):", start)

i = 0
arr = [0] * 10
while i < 10:
	# Take input from the user
	arr[i] = int(input())
	i = i + 1

# Print the user input
print(arr)

# Get the value of
# monotonic clock
# using time.monotonic() method
end = time.monotonic()

# print the value of
# the monotonic clock
print("\nAt the end of the process")
print("Value of the monotonic clock (in fractional seconds):", end)
print("Time elapsed during the process:", end - start)
