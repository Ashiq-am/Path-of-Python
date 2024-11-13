# Python program to explain time.clock_gettime_ns() method

# importing time module
import time


# clk_id for System-wide real-time clock
clk_id1 = time.CLOCK_REALTIME

# clk_id for monotonic clock
clk_id2 = time.CLOCK_MONOTONIC

# clk_id for monotonic (Raw hardware
# based time) clock
clk_id3 = time.CLOCK_MONOTONIC

# clk_id for Thread-specific CPU-time clock
clk_id4 = time.CLOCK_THREAD_CPUTIME_ID

# clk_id for High-resolution
# per-process timer from the CPU
clk_id5 = time.CLOCK_PROCESS_CPUTIME_ID


# Get the time (in nanoseconds) of the above
# specified clock clk_ids
# using time.clock_gettime_ns() method
t1 = time.clock_gettime_ns(clk_id1)
t2 = time.clock_gettime_ns(clk_id2)
t3 = time.clock_gettime_ns(clk_id3)
t4 = time.clock_gettime_ns(clk_id4)
t5 = time.clock_gettime_ns(clk_id5)


# Print the time (in nanoseconds) of
# different clock clk_ids
print("System-wide real-time clock time: % d nanoseconds" % t1)
print("Monotonic clock time: % d nanoseconds" % t2)
print("Monotonic (raw-hardware based) clock time: % d nanoseconds" % t3)
print("Thread-specific CPU time clock: % d nanoseconds" % t4)
print("Per-process timer from the CPU: % d nanoseconds" % t5)
