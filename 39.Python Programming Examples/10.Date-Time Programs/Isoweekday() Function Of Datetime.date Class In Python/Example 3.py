# importing the datetime module
import datetime

# Creating an dictionary with the return
# value as keys and the day as the value
# This is used to retrive the day of the week
# using the return value of the isoweekday()
# function
DaysList = ["None",
			"Monday",
			"Tuesday",
			"Wednesday",
			"Thursday",
			"Friday",
			"Saturday",
			"Sunday"]

# Getting the user's input
day = 1
month = 1
year = 2021
day_fallen = "Friday"

# Creating the datetime object for the user's
# input by using the date() function of datetime
# class
Date = datetime.date(year, month, day)

# Using the isoweekday() function
# to retrive the day of the given date
day = Date.isoweekday()

# Checking if the day is matching the user's
# day
if day_fallen.lower() == DaysList[day].lower():
	print("Yes, your given date", Date,
		"falls on your expected day i.e ",
		DaysList[day])
else:
	print("No, your given date", Date, "falls on",
		DaysList[day],
		"but not on", day_fallen)
