# importing pandas as pd
import pandas as pd
from datetime import datetime

# Create the Timedelta object
td = pd.Timedelta('7 days 15 hours')

# Print the Timedelta object

print(td.ceil('D'))
