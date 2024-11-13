# Python program to explain time.clock() method

# importing time module
import time


# Function to calculate factorial
# of the given number
def factorial(n):
    f = 1
    for i in range(n, 1, -1):
        f = f * i

    return f


# Get the current processor time
# in seconds at the
# beginning of the calculation
# using time.clock() method
start = time.clock()

# print the processor time in seconds
print("At the beginning of the calculation")
print("Processor time (in seconds):", start, "\n")

# Calculate factorial of all
# numbers form 0 to 9
i = 0
fact = [0] * 10

while i < 10:
    fact[i] = factorial(i)
    i = i + 1

# Print the calculated factorial
for i in range(0, len(fact)):
    print("Factorial of % d:" % i, fact[i])

# Get the processor time
# in seconds at the end
# of the calculation
# using time.clock() method
end = time.clock()

print("\nAt the end of the calculation")
print("Processor time (in seconds):", end)
print("Time elapsed during the calculation:", end - start)
