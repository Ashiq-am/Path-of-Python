import pendulum

# Create a Pendulum DateTime object
dt = pendulum.now()

# Convert to time string
time_string = dt.to_time_string()

print("Time String:", time_string)
