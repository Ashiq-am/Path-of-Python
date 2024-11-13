# importing the datetime module
import datetime

# Getting current date and time using now()
# function of the datetime class
todays_date = datetime.datetime.now()
print("Today's date and time:", todays_date)

# Replacing todays_date hour with 3 and day
# with 10 using replace() function using hour
# and day parameter
modified_date = todays_date.replace(day = 10, hour=3)
print("Modified date and time:", modified_date)
