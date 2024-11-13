# Python3 code for getting
# integer value corresponding
# to the specified day of the week.

# Importing datetime module
import datetime

# Mapping of the week day
weekDaysMapping = ("Monday", "Tuesday",
				"Wednesday", "Thursday",
				"Friday", "Saturday",
				"Sunday")

# Specifing a date and time value
dateTimeInstance = datetime.datetime(2021, 8, 2,
									00, 00, 00)

# Calling the weekday() function over the above
# specified weekday and data time value
dayOfTheWeek = weekDaysMapping[dateTimeInstance.weekday()]

# Printing the date and time along with the
# corresponding week day name
print("{} is for {}".format(dateTimeInstance, dayOfTheWeek))

# Getting on next day
nextDay = dateTimeInstance.replace(day=3)

# Calling the weekday() function over the above
# specified weekday and data time value
dayOfTheWeek = weekDaysMapping[nextDay.weekday()]

# Printing the date and time along with the
# corresponding week day name
print("{} is for {}".format(nextDay, dayOfTheWeek))

# Getting on next day
nextDay = dateTimeInstance.replace(day=4)

# Calling the weekday() function over the above
# specified weekday and data time value
dayOfTheWeek = weekDaysMapping[nextDay.weekday()]

# Printing the date and time along with the
# corresponding week day name
print("{} is for {}".format(nextDay, dayOfTheWeek))

# Getting on next day
nextDay = dateTimeInstance.replace(day=5)

# Calling the weekday() function over the above
# specified weekday and data time value
dayOfTheWeek = weekDaysMapping[nextDay.weekday()]

# Printing the date and time along with the
# corresponding week day name
print("{} is for {}".format(nextDay, dayOfTheWeek))

# Getting on next day
nextDay = dateTimeInstance.replace(day=6)

# Calling the weekday() function over the above
# specified weekday and data time value
dayOfTheWeek = weekDaysMapping[nextDay.weekday()]

# Printing the date and time along with the
# corresponding week day name
print("{} is for {}".format(nextDay, dayOfTheWeek))

# Getting on next day
nextDay = dateTimeInstance.replace(day=7)

# Calling the weekday() function over the above
# specified weekday and data time value
dayOfTheWeek = weekDaysMapping[nextDay.weekday()]

# Printing the date and time along with the
# corresponding week day name
print("{} is for {}".format(nextDay, dayOfTheWeek))

# Getting on next day
nextDay = dateTimeInstance.replace(day=8)

# Calling the weekday() function over the above
# specified weekday and data time value
dayOfTheWeek = weekDaysMapping[nextDay.weekday()]

# Printing the date and time along with the
# corresponding week day name
print("{} is for {}".format(nextDay, dayOfTheWeek))
