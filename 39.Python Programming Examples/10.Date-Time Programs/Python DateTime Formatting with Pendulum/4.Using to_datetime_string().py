import pendulum

# Create a Pendulum DateTime object
dt = pendulum.now()

# Convert to datetime string
datetime_string = dt.to_datetime_string()

print("Datetime String:", datetime_string)
