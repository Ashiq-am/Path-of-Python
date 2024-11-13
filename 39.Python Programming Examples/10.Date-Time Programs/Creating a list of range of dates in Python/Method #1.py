# Python3 code to demonstrate working of
# Get Construct Next K dates List
# Using timedelta() + list comphehension
import datetime

# initializing date
test_date = datetime.datetime(1997, 1, 4)

# printing original date
print("The original date is : " + str(test_date))

# initializing K
K = 5

# timedelta() gets successive dates with
# appropriate difference
res = [test_date + datetime.timedelta(days=idx) for idx in range(K)]

# printing result
print("Next K dates list : " + str(res))
