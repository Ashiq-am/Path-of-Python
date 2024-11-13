import datetime

date_example = "8/6/2021, 05:54:8"
date_format = datetime.datetime.strptime(date_example,
										"%m/%d/%Y, %H:%M:%S")
unix_time = datetime.datetime.timestamp(date_format)
print(unix_time)
