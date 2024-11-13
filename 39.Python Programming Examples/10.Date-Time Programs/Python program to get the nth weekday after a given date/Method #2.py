# Python3 code to demonstrate working of
# Next weekday from Date
# Using lamnda function
import datetime

# initializing dates
test_date = datetime.datetime(2017, 3, 14)

# printing original date
print("The original date is : " + str(test_date)[:10])

# initializing weekday index
weekday_idx = 4

# lambda function provides one liner shorthand
def lfnc(test_date, weekday_idx): return test_date + \
	datetime.timedelta(days=(weekday_idx - test_date.weekday() + 7) % 7)


res = lfnc(test_date, weekday_idx)

# printing result
print("Next date of required weekday : " + str(res)[:10])
