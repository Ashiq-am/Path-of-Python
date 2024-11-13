# Python3 code to demonstrate
# Getting a string containing
# the date and time

# Importing datetime and time module
import datetime
import time

# Calling the time() function
# to return current time
Todays_time = time.time()

# Printing today's time
print(Todays_time)

# Calling the fromtimestamp() function
# to get date from the current time
date_From_CurrentTime = datetime.date.fromtimestamp(Todays_time);

# Printing the current date
print("Date for Timestamp used is: %s"%date_From_CurrentTime);

# Calling the ctime() function over the above date
print("Today's date: %s"%date_From_CurrentTime.ctime());
