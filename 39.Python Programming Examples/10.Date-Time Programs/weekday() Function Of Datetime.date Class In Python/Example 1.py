# Python3 code for getting
# integer value corresponding
# to the specified day of the week

# Importing datetime module
import datetime

# Specifing some date and time values
dateTimeInstance1 = datetime.datetime(2021, 8, 1, 00, 00, 00)
dateTimeInstance2 = datetime.datetime(2021, 8, 2, 00, 00, 00)
dateTimeInstance3 = datetime.datetime(2021, 8, 3, 00, 00, 00)

# Calling the weekday() functions over the
# above dateTimeInstances
dayOfTheWeek1 = dateTimeInstance1.weekday()
dayOfTheWeek2 = dateTimeInstance2.weekday()
dayOfTheWeek3 = dateTimeInstance3.weekday()

# Getting the integer value corresponding
# to the specified day of the week
print(dayOfTheWeek1)
print(dayOfTheWeek2)
print(dayOfTheWeek3)
