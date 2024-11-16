from datetime import datetime

# Convert a string to a datetime object
date_string = '2023-07-17'
dateTime = datetime.strptime(date_string, '%Y-%m-%d')
print(dateTime)
