# import perf_counter_ns()
from time import perf_counter_ns

# integer input from user, 2 input in single line
n, m = map(int, input().split())

# Start the stopwatch / counter
start = perf_counter_ns()

for i in range(n):
	t = int(input()) # user gave input n times
	if t % m == 0:
		print(t)

# Stop the stopwatch / counter
stop = perf_counter_ns()

print("Elapsed time:", stop, 'ns', start, 'ns')

print("Elapsed time during the whole program",
	stop-start, 'ns')

