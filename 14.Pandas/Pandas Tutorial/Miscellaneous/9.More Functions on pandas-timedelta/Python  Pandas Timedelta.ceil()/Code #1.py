# importing pandas as pd
import pandas as pd
import datetime

# Create the Timedelta object
td = pd.Timedelta(5.05, unit ='s')

# Print the Timedelta object

print(td.ceil('S'))
