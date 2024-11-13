# importing the datetime module
import datetime

# Creating an dictionary with the return
# value as keys and the day as the value
# This is used to retrive the day of the
# week using the return value of the
# isoweekday() function
weekdays = {1: "Monday",
			2: "Tuesday",
			3: "Wednesday",
			4: "Thrusday",
			5: "Friday",
			6: "Saturday",
			7: "Sunday"}

# Getting current date using today()
# function of the datetime class
todays_date = datetime.date.today()
print("Today's date is :", todays_date)

# Using the isoweekday() function to
# retrive the day of the given date
day = todays_date.isoweekday()
print("The date", todays_date, "falls on",
	weekdays[day])
