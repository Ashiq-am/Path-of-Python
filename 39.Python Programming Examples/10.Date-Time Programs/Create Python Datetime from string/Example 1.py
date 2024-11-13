from datetime import datetime

input_str = '21/01/24 11:04:19'

dt_object = datetime.strptime(
input_str, '%d/%m/%y %H:%M:%S')

print("The type of the input date string now is: ",
	type(dt_object))

print("The date is", dt_object)
