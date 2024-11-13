from datetime import datetime

# By using now(), We will get both current
# date and time Storing current time and
# date into a variable
today = datetime.now()

# Storing the date and time you want to calculate
# In this you have to give the time as the input
graduation_day = datetime(2023, 8, 11, 0, 0, 0)

# finding the difference from
days_left = abs(graduation_day - today)

# Displaying the no.of.days left with time
print(f"Time left till the graduation: {days_left}")
