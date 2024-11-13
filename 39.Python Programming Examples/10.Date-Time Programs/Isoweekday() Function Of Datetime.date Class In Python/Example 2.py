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
day = 18
month = 9
year = 2020

# Creating the datetime object for the user's
# input by using the date() function of datetime
# class
Date = datetime.date(year, month, day)

# Using the isoweekday() function
# to retrive the day of the given date
day = Date.isoweekday()

print("The given date", Date, "falls on",
	DaysList[day])
