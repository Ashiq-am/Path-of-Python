# Python program to explain time.process_time_ns() method

# importing time module
import time

# Get the sum of the system
# and user CPU time of
# the current process in nanoseconds
# using time.process_time_ns() method
start = time.process_time_ns()

print("At the beginning of first example")
print("Process Time (in nanoseconds):", start, "\n")
# Here process time means sum of the system
# and user CPU time of the current process

# Print all natural numbers
# from 1 to 50

# assigning n = 50
n = 50

for i in range(1, n + 1):
    print(i, end=' ')

print()

end = time.process_time_ns()

print("\nAt the end of the first example")
print("Process time (in nanoseconds):", end)
print("Elapsed time during the first example (in nanoseconds):", end - start)

# Get the sum of the system
# and user CPU time of
# the current process in nanoseconds
# using time.process_time_ns() method
start = time.process_time_ns()

print("\nAt the beginning of second example")
print("Process Time (in nanoseconds):", start, "\n")
# Here process time means sum of the system
# and user CPU time of the current process

# Print all natural numbers
# from 1 to 50

# assigning n = 100
n = 50

for i in range(1, n + 1):
    print(i, end=' ')

print()

# suspend the execution of the current
# process for 10 seconds
time.sleep(10)

end = time.process_time_ns()
print("\nAt the end of the second example")
print("Process time (in nanoseconds):", end)
print("Elapsed time during the second example (in nanoseconds):", end - start)

# In both the examples
# we can see (in the output below)
# that elapsed time
# is more or less the same
# so, the suspension of process for
# 10 seconds is not included
