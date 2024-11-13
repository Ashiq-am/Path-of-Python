# Python3 code to demonstrate working of
# Last weekday of every month in year
# Using list comprehension
import calendar

# initializing year
year = 1997

# printing Year
print("The original year : " + str(year))

# initializing weekday
weekdy = 5

# list comprehension for shorthand
res = [str(max(week[weekdy]
			for week in calendar.monthcalendar(year, month))) +
	"/" + str(month)+ "/" + str(year) for month in range(1, 13)]

# printing
print("Last weekdays of year : " + str(res))
