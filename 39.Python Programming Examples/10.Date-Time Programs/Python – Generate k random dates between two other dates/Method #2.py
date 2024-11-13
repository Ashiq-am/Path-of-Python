# Python3 code to demonstrate working of
# Random K dates in Range
# Using randrange() + timedelta() + loop
from datetime import date, timedelta
import random

# initializing dates ranges
test_date1, test_date2 = date(2015, 6, 3), date(2015, 7, 1)

# printing dates
print("The original range : " + str(test_date1) + " " + str(test_date2))

# initializing K
K = 7

# getting days between dates
dates_bet = test_date2 - test_date1
total_days = dates_bet.days

res = []
for idx in range(K):
    random.seed(a=None)

    # getting random days
    randay = random.randrange(total_days)

    # getting random dates
    res.append(test_date1 + timedelta(days=randay))

# printing
print("K random dates in range : " + str(res))
