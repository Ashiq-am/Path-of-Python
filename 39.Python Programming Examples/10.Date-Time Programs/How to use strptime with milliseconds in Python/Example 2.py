from datetime import datetime

# Getting current datetime and converting
# it to string
date_str = str(datetime.now())

print(type(date_str))

print(datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f'))
