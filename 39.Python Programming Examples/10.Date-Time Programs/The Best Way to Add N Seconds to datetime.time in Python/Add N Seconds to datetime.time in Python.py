from datetime import datetime, time, timedelta

# 23:59 or 11:59 PM
initial_time = time(23, 59)

current_date = datetime.now().date()
datetime_combination = datetime.combine(current_date, initial_time)

# Adding 35 seconds
seconds_to_add = 35
new_datetime = datetime_combination + timedelta(seconds=seconds_to_add)

new_time = new_datetime.time()
print("New Time:", new_time)
