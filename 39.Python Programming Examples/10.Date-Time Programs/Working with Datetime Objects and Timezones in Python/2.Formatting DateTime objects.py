# importing datetime object
import datetime

# initialising datetime object
obj = datetime.datetime(2001, 12, 9)

# Example 1
print(obj.strftime("%a %m %y"))

# Example 2
print(obj.strftime("%m-%d-%Y %T:%M%p"))
