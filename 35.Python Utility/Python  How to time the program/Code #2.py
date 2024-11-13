# using the class Timer()
def countdown(n):
    while n > 0:
        n -= 1


# Use 1: Explicit start / stop
time = Timer()

# start
time.start()
countdown(1000000)

# stop
time.stop()
print(time.elapsed)

# Use 2: As a context manager
with time:
    countdown(1000000)

print(time.elapsed)

with Timer() as t2:
    countdown(1000000)

print(t2.elapsed)
