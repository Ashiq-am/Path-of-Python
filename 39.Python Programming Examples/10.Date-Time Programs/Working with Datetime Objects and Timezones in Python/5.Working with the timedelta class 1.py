# importing datetime and pytz
import datetime
import pytz

# defining the objects
obj = datetime.datetime(2001, 11, 15, 1, 20, 25)

# defining a timedeta
diff = datetime.timedelta(days=90, hours=1)

# getting a datetime object
# that is 90 days and 1 hour ahead
new_obj = obj+diff

# Our final answer
print(new_obj)
