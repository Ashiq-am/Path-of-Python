import datetime

# Creating a date object
date_object = datetime.date(2024, 7, 17)

# Getting the day name
day_name = date_object.strftime("%A")

# Printing the day name
print(f"The day name for {date_object} is: {day_name}")
