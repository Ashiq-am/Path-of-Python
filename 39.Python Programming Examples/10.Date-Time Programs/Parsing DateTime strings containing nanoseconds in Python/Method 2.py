import pandas as pd

# Parse the timestamp string by
# providing the format of timestamp string
dt_obj = pd.to_datetime("2021-08-05 15:25:56.792554",
						format="%Y-%m-%d %H:%M:%S.%f")

# Verify the value for nano seconds
nano_secs = dt_obj.strftime("%f")

# Print the value of nano seconds
print(nano_secs)
