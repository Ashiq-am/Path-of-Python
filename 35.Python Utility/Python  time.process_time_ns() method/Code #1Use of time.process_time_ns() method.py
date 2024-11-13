# Python program to explain time.process_time_ns() method

# importing time module
import time

# assigning n = 100
n = 100

# Get the sum of the system
# and user CPU time of
# the current process in nanoseconds
# using time.process_time_ns() method
start = time.process_time_ns()

print("At the beginning of the process")
print("Process Time (in nanoseconds):", start, "\n")
# Here process time means sum of the system
# and user CPU time of the current process


# Print all natural numbers
# from 1 to 100

for i in range(1, n + 1):
    print(i, end=' ')

print()

end = time.process_time_ns()

print("\nAt the end of the process")
print("Process time (in nanoseconds):", end)
print("Elapsed time during the process (in nanoseconds):", end - start)
