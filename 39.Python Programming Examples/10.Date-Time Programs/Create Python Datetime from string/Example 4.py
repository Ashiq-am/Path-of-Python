from datetime import datetime

time_str = '220917 114519'
dt_obj = datetime.strptime(time_str, '%d/%m/%y %H:%M:%S')

print ("The type is", type(dt_obj))
print ("The date is", date_time_obj)
