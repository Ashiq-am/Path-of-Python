# importing pandas as pd
import pandas as pd

# Create the Timedelta object
td = pd.Timedelta('1 days 7 hours 254.1245 seconds')

# Print the Timedelta object
print(td)

print(td.microseconds)
