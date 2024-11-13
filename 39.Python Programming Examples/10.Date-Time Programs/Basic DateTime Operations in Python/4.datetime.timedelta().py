from datetime import timedelta, datetime

present_date_with_time = datetime.now()

print("Present Date :", present_date_with_time)

# coming date after 10 days
ten_days_after= present_date_with_time + timedelta(days = 10)
print('Date after 10 days :',ten_days_after)

# date before 10 days
ten_days_before= present_date_with_time - timedelta(days = 10)
print('Date before 10 days :',ten_days_before)

# date before one year ago
one_year_before_today= present_date_with_time + timedelta(days = 365)
print('One year before present Date :', one_year_before_today)

#date before one year ago
one_year_after_today= present_date_with_time - timedelta(days = 365)
print('One year before present Date :', one_year_after_today)

print("\n")
print("print some other attributes of timedelta\n")

# maximum days and time
print("Max : ",timedelta.max)

# miniimum days and time
print("Min : ",timedelta.min)

# The smallest possible difference between non-equal
# timedelta objects, timedelta(microseconds=1)
print("Resolution: ",timedelta.resolution)

print('Total number of seconds in an year :',
	timedelta(days = 365).total_seconds())

print("\nApply some operations on timedelta function\n")
time_after_one_min = present_date_with_time + timedelta(seconds=10) * 6
print('Time after one minute :', time_after_one_min)

print('Timedelta absolute value :', abs(timedelta(days = +20)))

print('Timedelta string representation :', str(timedelta(days = 5,
					seconds = 40, hours = 20, milliseconds = 355)))

print('Timedelta object representation :', repr(timedelta(days = 5,
					seconds = 40, hours = 20, milliseconds = 355)))
