# importing pandas as pd
import pandas as pd

# Create the Timedelta object
td = pd.Timedelta('7 days 15 min 3 s 42 ns')

# Print the Timedelta object
print(td)

print(td.nanoseconds)
