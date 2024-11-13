# Importing the datetime module
import datetime
import pytz

# Storing the current date and time in
# a new variable using the datetime.now()
# function of datetime module and adding the timezone
# using timezone function of pytz module.
current_date = datetime.datetime.now(pytz.timezone('Africa/Abidjan'))

# Printing the value of current_date
print(current_date)
