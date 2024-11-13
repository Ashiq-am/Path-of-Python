# import datetime
from datetime import datetime


# Create two dates with year, month,
# date, hour, minute, seconds
d1 = datetime(2021, 3, 16, 19, 6, 6)
d2 = datetime(2021, 3, 31, 12, 2, 2)

# Difference between two dates
diff = d2 - d1

print("Difference: ", diff)
