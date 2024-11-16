# importing pandas module
import pandas as pd

# using date_range function to generate
# dates from january 1 2021 to
# march 16 2021 as periods = 75
dates = pd.date_range('1/1/2021', periods=75)

print(dates)
