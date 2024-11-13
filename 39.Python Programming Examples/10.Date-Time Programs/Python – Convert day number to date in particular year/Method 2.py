# Python3 code to demonstrate working of
# Convert day number to date in particular year
# Using datetime.strptime()
from datetime import datetime, date, timedelta

# initializing day number
day_num = "339"

# print day number
print("The day number : " + str(day_num))

# adjusting day num
day_num.rjust(3 + len(day_num), '0')

# Initialize year
year = "2020"

# Initializing start date
strt_date = date(int(year), 1, 1)

# converting to date
res_date = strt_date + timedelta(days=int(day_num) - 1)
res = res_date.strftime("%m-%d-%Y")

# printing result
print("Resolved date : " + str(res))
