def accumulator():
    total = 0
    while True:

        # Yield the current total
        value = yield total
        # Add the received value to the total
        total += value

# Create the coroutine
acc = accumulator()

# Start the coroutine
next(acc)

# Send values and print the accumulated total
print(acc.send(5))
print(acc.send(10))
print(acc.send(20))
