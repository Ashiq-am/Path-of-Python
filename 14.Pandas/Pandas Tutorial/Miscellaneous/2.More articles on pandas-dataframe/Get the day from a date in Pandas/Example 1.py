# importing the module
import pandas as pd

# the date in "dd/mm/yyyy" format
date = "19/02/2022"
print("Initially the type is : ", type(date))

# converting string to DataTime
date = pd.to_datetime(date, format = "%d/%m/%Y")
print("After conversion, the type is : ", type(date))

# fetching the day
print("The day is : " + date.day_name())
