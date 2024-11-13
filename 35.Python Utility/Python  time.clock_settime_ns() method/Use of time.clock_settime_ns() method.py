# Python program to explain time.clock_settime_ns() method

# importing time module
import time


# clk_id for System-wide real-time clock
clk_id = time.CLOCK_REALTIME


# Get the current value of
# system-wide real-time clock (in nanoseconds)
# using time.clock_gettime_ns() method
t = time.clock_gettime_ns(clk_id)

print("Current value of system-wide real-time clock: % d nanoseconds" % t)

# Set the new value of
# time (in nanoseconds) for
# System-wide real-time clock
# using time.clock_settime_ns() method
nanosecs = 10000000
time.clock_settime(clk_id, nanosecs)

print("\nTime modified")


# Get the modified value of
# system-wide real-time clock (in nanoseconds)
# using time.clock_gettime_ns() method
t = time.clock_gettime_ns(clk_id)
print("\nCurrent value of system-wide real-time clock: % d nanoseconds" % t)
