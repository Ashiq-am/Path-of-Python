import datetime

# Taking date input from the user
date_str = input("Enter a date (YYYY-MM-DD format): ")
date_object = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

# Getting the day name
day_name = date_object.strftime("%A")

# Printing the day name
print(f"The day name for {date_object} is: {day_name}")
