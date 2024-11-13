import pendulum

# Create a Pendulum DateTime object
dt = pendulum.now()

# Convert to datetime string with day
day_datetime_string = dt.format('dddd, MMMM DD YYYY HH:mm:ss')

print("Datetime String with Day:", day_datetime_string)
