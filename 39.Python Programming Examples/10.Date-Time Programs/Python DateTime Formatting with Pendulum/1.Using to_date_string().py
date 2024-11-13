import pendulum

# Create a Pendulum DateTime object
dt = pendulum.now()

# Convert to date string
date_string = dt.to_date_string()

print("Date String:", date_string)
