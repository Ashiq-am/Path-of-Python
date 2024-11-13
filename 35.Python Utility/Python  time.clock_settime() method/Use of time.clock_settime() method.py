# Python program to explain time.clock_settime() method

# importing time module
import time


# clk_id for System-wide real-time clock
clk_id = time.CLOCK_REALTIME


# Get the current value of
# system-wide real-time clock (in seconds)
# using time.clock_gettime() method
t = time.clock_gettime(clk_id)

print("Current value of system-wide real-time clock: % d seconds" % t)

# Set the new value of
# time (in seconds) for
# System-wide real-time clock
# using time.clock_settime() method
seconds = 10000000
time.clock_settime(clk_id, seconds)

print("\nTime modified")


# Get the modified value of
# system-wide real-time clock (in seconds)
# using time.clock_gettime() method
t = time.clock_gettime(clk_id)
print("\nCurrent value of system-wide real-time clock: % d seconds" % t)
