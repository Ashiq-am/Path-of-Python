# Python3 code to demonstrate working of
# Last business day
# using max() + % operator + timedelta()
from datetime import datetime, timedelta

# initializing dates
test_date = datetime(2020, 1, 31)

# printing original date
print("The original date is : " + str(test_date))

# getting difference
# using max() to get differences
diff = max(1, (test_date.weekday() + 6) % 7 - 3)

# subtracting diff
res = test_date - timedelta(days=diff)

# printing result
print("Last business day : " + str(res))
