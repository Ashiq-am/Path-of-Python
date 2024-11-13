# Python3 code to demonstrate
# attributes of now() for timezone

# for now()
import datetime

# for timezone()
import pytz

# using now() to get current time
current_time = datetime.datetime.now(pytz.timezone('Asia/Dhaka'))

# printing current time in india
print("The current time in Bangladesh is : ")
print(current_time)
