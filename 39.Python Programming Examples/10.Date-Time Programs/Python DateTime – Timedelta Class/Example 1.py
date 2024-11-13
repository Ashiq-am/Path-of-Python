# Timedelta function demonstration

from datetime import datetime, timedelta

# creating dateime objects
date1 = datetime(2020, 1, 3)
date2 = datetime(2020, 2, 3)

# difference between dates
diff = date2 - date1
print("Difference in dates:", diff)

# Adding days to date1
date1 += timedelta(days = 4)
print("Date1 after 4 days:", date1)

# Sutracting days from date1
date1 -= timedelta(15)
print("Date1 before 15 days:", date1)
