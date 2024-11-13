# Python program to explain time.clock_getres() method

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


# Get the precision (Resolution)
# of the above specified clock clk_ids
# using time.clock_getres() method
precision1 = time.clock_getres(clk_id1)
precision2 = time.clock_getres(clk_id2)

# Print the precision (resolution)
print("Precision of system-wide real-time clock:", precision1)
print("Precision of monotonic clock:", precision2)
