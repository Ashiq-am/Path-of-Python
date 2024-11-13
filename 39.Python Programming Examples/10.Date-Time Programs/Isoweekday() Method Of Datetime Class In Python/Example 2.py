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

# Getting current year using today() function
# of the datetime class and the year attribute
Today = datetime.date.today()
current_year = Today.year

for i in range(2010, current_year+1):
	# Printing the day of the year
	# by first creating an datetime object
	# for the starting day of the year and
	# then we use isoweekday
	# to get the value and we use the
	# weekdays to retrive the day of the year
	print("The {}/{} in the year {} has fallen on {}".\
		format(Today.month, Today.day, i,
		weekdays[datetime.date(i, Today.month,
					Today.day).isoweekday()]))
