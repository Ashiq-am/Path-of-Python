# Python3 code to demonstrate working of
# Get Last date of Month
# Using replace() + timedelta()
import datetime

# initializing date
test_date = datetime.datetime(2018, 6, 4)

# printing original date
print("The original date is : " + str(test_date))

# getting next month
# using replace to get to last day + offset
# to reach next month
nxt_mnth = test_date.replace(day=28) + datetime.timedelta(days=4)

# subtracting the days from next month date to
# get last date of current Month
res = nxt_mnth - datetime.timedelta(days=nxt_mnth.day)

# printing result
print("Last date of month : " + str(res.day))
