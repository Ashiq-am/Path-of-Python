from datetime import datetime

time_str = '201123101455'

dt_obj = datetime.strptime(time_str, '%y%m%d%H%M%S')
dt_obj2 = datetime.strptime(time_str, '%d%m%y%H%S%M')

print ("1st interpretation of date from string is: ",dt_obj)
print ("2nd interpretation of date from same string is", dt_obj2)
