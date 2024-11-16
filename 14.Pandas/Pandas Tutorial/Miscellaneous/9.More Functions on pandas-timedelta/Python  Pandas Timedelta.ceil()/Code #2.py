# importing pandas as pd
import pandas as pd
import datetime

# Create the Timedelta object
td = pd.Timedelta(13.25, unit ='h')

# Print the Timedelta object

print(td.ceil('H'))
