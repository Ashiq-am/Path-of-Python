# importing pandas as pd
import pandas as pd

# Create the Timedelta object
td = pd.Timedelta('3 days 06:05:01.000030')

# Print the Timedelta object
print(td)

print(td.components)
