# importing datetime class
from datetime import datetime

# Creating an instance of datetime.
dateIs = datetime(1, 1, 1, 0, 0, 0, 0)

# Using toordinal() method
toOrdinal = dateIs.toordinal()
print(f"Ordinal value of Earliest Datetime {dateIs} is {toOrdinal}")

print()

dateIs = datetime(9999, 12, 31, 23, 59, 59)
toOrdinal = dateIs.toordinal()
print(f"Ordinal value of Latemost Datetime {dateIs} is {toOrdinal}")
