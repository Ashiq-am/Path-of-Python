# Python3 code to demonstrate working of
# Get Construct Next K dates List
# Using count() + generator function
import datetime
import itertools

# initializing date
test_date = datetime.datetime(1997, 1, 4)

# printing original date
print("The original date is : " + str(test_date))

# initializing K
K = 5

# timedelta() gets successive dates with
# appropriate difference
gen_fnc = (
    test_date - datetime.timedelta(days=idx) for idx in itertools.count())

# islice passes counter
res = itertools.islice(gen_fnc, K)

# printing result
print("Next K dates list : " + str(list(res)))
