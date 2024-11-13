# import datetime
from datetime import date


# Create two dates with year, month,
# date
d1 = date(2021, 3, 16)
d2 = date(2021, 3, 31)

# Difference between two dates
diff = d2 - d1

print("Difference: ", diff.days)
