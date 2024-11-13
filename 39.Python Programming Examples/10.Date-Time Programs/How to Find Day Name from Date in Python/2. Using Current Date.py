import datetime

# Getting current date
current_date = datetime.date.today()

# Getting the day name
day_name = current_date.strftime("%A")

# Printing the day name
print(f"Today is: {day_name}")
