# Python3 code to demonstrate working of
# Convert date range to N equal durations
# Using generator function
import datetime


def group_util(test_date1, test_date2, N):
    diff = (test_date2 - test_date1) / N
    for idx in range(N):
        # using generator function to solve problem
        # returns intermediate result
        yield (test_date1 + diff * idx)
    yield test_date2


# initializing dates
test_date1 = datetime.datetime(1997, 1, 4)
test_date2 = datetime.datetime(1997, 1, 30)

# printing original dates
print("The original date 1 is : " + str(test_date1))
print("The original date 2 is : " + str(test_date2))

# initializing N
N = 7

# calling generator expression
temp = list(group_util(test_date1, test_date2, N))

# using strftime to convert to userfriendly format
res = []
for sub in temp:
    res.append(sub.strftime("%Y/%m/%d %H:%M:%S"))

# printing result
print("N equal duration dates : " + str(res))
