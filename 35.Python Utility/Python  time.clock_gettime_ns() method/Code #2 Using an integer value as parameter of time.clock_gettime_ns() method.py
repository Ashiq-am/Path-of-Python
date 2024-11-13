# Python program to explain time.clock_gettime_ns() method

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


# Get the time in nanoseconds)
# for the specified clock clk_ids
# using time.clock_gettime_ns() method
t1 = time.clock_gettime_ns(clk_id1)
t2 = time.clock_gettime_ns(clk_id2)

# Print the time in nanoseconds
print("System-wide real-time clock time: % d nanoseconds" % t1)
print("Monotonic clock time: % d nanoseconds" % t2)
