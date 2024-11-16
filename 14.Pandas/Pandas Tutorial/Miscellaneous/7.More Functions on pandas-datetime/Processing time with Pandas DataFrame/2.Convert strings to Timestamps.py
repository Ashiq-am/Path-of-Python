# Load libraries
import numpy as np
import pandas as pd

# Create time Strings
dt_strings = np.array(['04-03-2019 12:35 PM',
					'22-06-2017 11:01 AM',
					'05-09-2009 07:09 PM'])

# Convert to datetime format
timestamps = [pd.to_datetime(date, format ="%d-%m-%Y%I:%M %p",
					errors ="coerce") for date in dt_strings]

# Convert to datetimes
timestamps = [pd.to_datetime(date, format ="%d-%m-%Y %I:%M %p",
					errors ="coerce") for date in dt_strings]
