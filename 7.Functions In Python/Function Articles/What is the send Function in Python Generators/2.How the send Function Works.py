def echo():
    while True:
        value = yield  # Wait for a value to be sent
        print(f"Received: {value}")

# Create a generator
generator = echo()

# Start the generator
next(generator)

# Send values to the generator
generator.send("Hello")
generator.send("World")
