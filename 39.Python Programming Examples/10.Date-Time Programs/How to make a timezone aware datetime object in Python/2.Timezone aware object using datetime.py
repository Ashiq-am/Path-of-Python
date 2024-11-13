# Importing the datetime module
import datetime

# Storing the current date and time in
# a new variable using the datetime.now()
# function of datetime module
current_date = datetime.datetime.now()

# Replacing the value of the timezone in tzinfo class of
# the object using the replace() function
current_date = current_date.\
	replace(tzinfo=datetime.timezone.utc)

# Converting the date value into ISO 8601
# format using isoformat() method
current_date = current_date.isoformat()

# Printing the value of current_date
print(current_date)
