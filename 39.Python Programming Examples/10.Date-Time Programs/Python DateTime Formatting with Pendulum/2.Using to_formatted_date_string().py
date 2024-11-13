import pendulum

# Create a Pendulum DateTime object
dt = pendulum.now()

# Convert to custom formatted date string
custom_date_string = dt.format("dddd, MMMM Do YYYY")

print("Custom Formatted Date String:", custom_date_string)
