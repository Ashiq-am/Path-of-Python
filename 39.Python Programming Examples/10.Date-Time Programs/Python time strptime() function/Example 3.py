import time as datetime

datetime_str = '08/1/18 3:55:6'

try:
	datetime_object = datetime.strptime(datetime_str, '%m/%d/%y')
except ValueError as e:
	print('ValueError Raised:', e)


time_str = '25::55::26'

try:
	time_object = datetime.time.strptime(time_str, '%H::%M::%S')
except ValueError as e:
	print('ValueError:', e)
