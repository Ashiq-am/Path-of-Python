# Importing date from Datetime module
from datetime import date

# Storing today's date into a variable
today = date.today()

# Storing the specific date
graduation_day = date(2023, 8, 11)

# finding the difference of today's date from
# specified date
days_left = abs(graduation_day - today)

# Displaying the no.of.days left without time
print(f"Number of days left till graduation: {days_left}")
