# Python program to show time by process_time_ns()
from time import process_time_ns

n = 50

# Start the stopwatch / counter
t1_start = process_time_ns()

for i in range(n):
	print(i, end =' ')

print()

# Stop the stopwatch / counter
t1_stop = process_time_ns()

print("Elapsed time:", t1_stop, t1_start)

print("Elapsed time during the whole program in nanoseconds:",
											t1_stop-t1_start)
