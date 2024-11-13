# importing datetime class
from datetime import datetime

# Creating an instance of datetime.
dateIs = datetime(189, 0, 0)

# Using toordinal() method
toOrdinal = dateIs.toordinal()
print(f"Ordinal value of Earliest Datetime {dateIs} is {toOrdinal}")
