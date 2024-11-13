from datetime import datetime
dtime = datetime(2018, 1, 1, 20)
print("Datetime: ", dtime)

dtimestamp = dtime.timestamp()
print("Integer timestamp in seconds: ",
	int(round(dtimestamp)))

milliseconds = int(round(dtimestamp * 1000))
print("Integer timestamp in miliseconds: ",
	milliseconds)
