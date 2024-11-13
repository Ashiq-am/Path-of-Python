# Importing the datetime module
import datetime
import pytz

# Storing the current date and time in
# a new variable using the datetime.now()
# function of datetime module and adding the timezone
# using timezone function of pytz module.
current_date = datetime.datetime.now(pytz.timezone('Africa/Abidjan'))

# Checking the timezone information of the
# object stored in tzinfo base class
if current_date.tzinfo == None or current_date. \
        tzinfo.utcoffset(current_date) == None:

    # If passes the above condition then
    # the object is unaware
    print("Unaware")
else:
    # Else printing "Aware"
    print("Aware")

# Printing the value of current_date
print(current_date)
