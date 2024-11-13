# Python program to explain time.clock_gettime() method

# importing time module
import time


# value of clk_id for time.CLOCK_REALTIME
# clock id constant which represents
# System-wide real-time clock is 0
clk_id1 = 0

# value of clk_id for time.CLOCK_MONOTONIC
# clock id constant which represents
# a monotonic clock is 2
clk_id2 = 2


# Get the time (in seconds)
# for the specified clock clk_ids
# using time.clock_gettime() method
t1 = time.clock_gettime(clk_id1)
t2 = time.clock_gettime(clk_id2)

# Print the time in seconds
print("Value of system-wide real-time clock time:", t1)
print("Value of monotonic clock time:", t2)
