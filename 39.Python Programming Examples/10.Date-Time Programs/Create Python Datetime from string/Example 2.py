from datetime import datetime

time_str = 'May 17 2019 11:33PM'
dt_object = datetime.strptime(
time_str, '%b %d %Y %I:%M%p')

print(dt_object)
