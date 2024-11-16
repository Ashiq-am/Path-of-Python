# importing pandas as pd
import pandas as pd
import datetime

# Create the Timedelta object
td = pd.Timedelta(datetime.timedelta(days = 3, hours = 7, seconds = 8))

# Print the Timedelta object
print(td)

print(td.asm8)
