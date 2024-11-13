from datetime import datetime

# Parse the default python timestamp format
dt_obj = datetime.strptime("2021-08-05 15:25:56.792554",
						"%Y-%m-%d %H:%M:%S.%f")

# Verify the value for nano seconds
nano_secs = dt_obj.strftime("%f")

# Print the value of nano seconds
print(nano_secs)
