# importing the datetime module
import datetime

# Getting current date using today()
# function of the datetime class
todays_date = datetime.date.today()
print("Original Date:", todays_date,)

# Trying to replace the todays_date hour
# with 3 using replace() function
modified_date = todays_date.replace(hour=3)
print("Modified Date:", modified_date)
