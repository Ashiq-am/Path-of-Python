# Python program to explain time.monotonic_ns() method

# importing time module
import time


# Function to calculate factorial
# of the given number
def factorial(n):
    f = 1
    for i in range(n, 1, -1):
        f = f * i

    return f


# Get the value of the
# monotonic clock in nanoseconds at the
# beginning of the process
# using time.monotonic_ns() method
start = time.monotonic_ns()

# print the value of
# the monotonic clock in nanoseconds
print("At the beginning of the process")
print("Value of the monotonic clock (in nanoseconds):", start, "\n")

# Calculate factorial of all
# numbers form 0 to 9
i = 0
fact = [0] * 10;

while i < 10:
    fact[i] = factorial(i)
    i = i + 1

# Print the calculated factorial
for i in range(0, len(fact)):
    print("Factorail of % d:" % i, fact[i])

# Get the value of
# monotonic clock in nanoseconds
# using time.monotonic_ns() method
end = time.monotonic_ns()

# print the value of
# the monotonic clock
print("\nAt the end of the process")
print("Value of the monotonic clock (in nanoseconds):", end)
print("Time elapsed during the process:", end - start)
