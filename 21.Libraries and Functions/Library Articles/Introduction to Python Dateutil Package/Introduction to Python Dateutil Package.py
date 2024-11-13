from dateutil import parser
from datetime import datetime

# Example date strings
date_str1 = "2024-09-16"
date_str2 = "16th September, 2024"
date_str3 = "09/16/2024"

# Parsing date strings
date1 = parser.parse(date_str1)
date2 = parser.parse(date_str2)
date3 = parser.parse(date_str3)

# Print parsed dates
print("Parsed Date 1:", date1)
print("Parsed Date 2:", date2)
print("Parsed Date 3:", date3)

# Calculating the difference between two dates
date_diff = date2 - date1
print("Difference between Date 2 and Date 1:", date_diff)
