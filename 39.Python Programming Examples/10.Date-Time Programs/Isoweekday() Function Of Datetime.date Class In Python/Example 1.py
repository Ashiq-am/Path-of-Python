# importing the datetime module
import datetime

# Creating an list which will
# be used to retrieve the day of the
# week using the return value of the
# isoweekday() function
DaysList = ["None",
			"Monday",
			"Tuesday",
			"Wednesday",
			"Thursday",
			"Friday",
			"Saturday",
			"Sunday"]

# Using the function today()
# to get today's date
CurrentDate = datetime.date.today()
print("Current Date is :", CurrentDate)

# Using the isoweekday() function to
# retrieve the day of the given date
day = CurrentDate.isoweekday()
print("The date", CurrentDate, "falls on",
	DaysList[day])
