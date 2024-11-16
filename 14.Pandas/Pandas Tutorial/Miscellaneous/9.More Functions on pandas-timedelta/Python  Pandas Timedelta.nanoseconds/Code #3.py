# importing pandas as pd
import pandas as pd
import datetime

# Create the Timedelta object
td = pd.Timedelta(133, unit ='ns')

# Print the Timedelta object
print(td)

print(td.nanoseconds)
