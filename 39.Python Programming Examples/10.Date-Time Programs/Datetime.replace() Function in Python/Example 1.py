# importing the datetime module
import datetime

# Getting current date using today()
# function of the datetime class
todays_date = datetime.date.today()
print("Original Date:", todays_date)

# Replacing the todays_date year with
# 2000 using replace() function
modified_date = todays_date.replace(year=2000)
print("Modified Date:", modified_date)
